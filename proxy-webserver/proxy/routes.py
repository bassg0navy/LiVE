import queue
from flask import redirect, render_template, request, Response, jsonify
from markupsafe import escape
from proxy import requests
from proxy import app, VIDEO_STORAGE_HOST, VIDEO_STORAGE_PORT, connection
#from proxy import create_engine
from proxy import cx_Oracle, sys, os, datetime, json
from proxy.send import rabbit_connection, channel
import pika
#from jinja2 import Template

#VARIABLES
#url = "http://{0}:{1}/video".format(VIDEO_STORAGE_HOST, VIDEO_STORAGE_PORT) <- URL For Remote Video
#url = "http://{0}:{1}/".format(VIDEO_STORAGE_HOST, VIDEO_STORAGE_PORT)

# DB ENGINE CONNECTION
#if sys.platform.startswith("darwin"):
    #cx_Oracle.init_oracle_client(
        #lib_dir=os.environ.get("HOME")+"/Downloads/instantclient_19_8",
        #config_dir="")
#elif sys.platform.startswith("win"):
    #cx_Oracle.init_oracle_client(
        #lib_dir=r"C:\Users\kabass\Oracle\instantclient-basiclite-windows.x64-21.3.0.0.0\instantclient_21_3")
        #lib_dir="/app/instantclient_21_3")
# else assume system library search path includes Oracle Client libraries
# On Linux, use ldconfig or set LD_LIBRARY_PATH, as described in installation documentation.

#with engine.connect() as conn:
#    print(conn.scalar("select sysdate from dual"))


'''
@app.route('/remote_video')
def _proxy():
    return redirect((url), code=302)
'''

@app.route('/home/', methods=['GET'])
def hello():
    return "Hello "

# NEED A WAY TO REQUEST VIDEO NAME FROM DB,  GIVEN THE ID FOR THE VIDEO THAT WAS REQUESTED AT THE '/REMOTE_VIDEO' 
# ROUTE

@app.route('/<video_streaming>/<VIDEO_ID>')
def _proxy(video_streaming, VIDEO_ID, *args, **kwargs):
    cur = connection.cursor()
    cur.execute("select video_name from video where video_id = :VIDEO_ID", VIDEO_ID=VIDEO_ID)
    res = cur.fetchone()
    VIDEO_NAME = res[0]
    URL = "http://{0}:{1}/{2}/{3}".format(VIDEO_STORAGE_HOST, VIDEO_STORAGE_PORT, video_streaming, VIDEO_NAME)
    #URL = "http://{0}:{1}/".format(VIDEO_STORAGE_HOST, VIDEO_STORAGE_PORT)
    resp = requests.request(
        method=request.method,
        url=(URL), #url=request.url.replace(request.host_url, (url)), 
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
        if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    timestamp = datetime.datetime.now()
    status = "viewed"
    myDict = {'video_name': VIDEO_NAME, 'status': status, 'timestamp': timestamp}
    json_dump = json.dumps(myDict, default=str)
    #r = requests.post('http://history-api:5002/history/viewed', json=(json_dump))
    channel.queue_declare(queue='viewed')
    channel.basic_publish(exchange='',
                      routing_key='viewed',
                      body=json_dump)
    print(" [x] Sent 'viewed message'")
    return response

# HOME PAGE
#app.route('/', methods=['GET'])
#def welcome():
#    return render_template('static.html')  # render a template

#@app.route('/local_video/<VIDEO_ID>', methods=['GET'])
#def video_streaming():
#    connection = cx_Oracle.connect(user="admin", password="$4THround4THround$", dsn="streamingdb1_high")
#    cur = connection.cursor()
#    cur.execute("select video_name from video where video_id = :VIDEO_ID", VIDEO_ID=VIDEO_ID)
#    res = cur.fetchone()
#    VIDEO_NAME = res[0]
#    return render_template('static_local.html', VIDEO_ID=VIDEO_ID, VIDEO_NAME=VIDEO_NAME, url=url)  # render a template