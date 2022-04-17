from flask import render_template, request, stream_with_context, Response, send_file, url_for
from markupsafe import escape
from storage import requests
from storage import oci, app, os
from jinja2 import Template
import urllib3
import urllib.request
import re
import pika

from oci.config import from_file
config = from_file(file_location="/app/.oci/abstract.conf")

# Initialize service client with default config file
object_storage_client = oci.object_storage.ObjectStorageClient(config)

# Send the request to service, some parameters are not required
# Should place object storage 'gets' in own py file as app scales


@app.route('/remote_video/<video_name>')
def remote_video(video_name):
    get_object_response = object_storage_client.get_object(
    namespace_name="id9ypxcsj7cu",
    bucket_name="streaming-videos",
    object_name="fam4330e84be1734f3b8f9bcc9df3bef1c8.mp4",
    http_response_content_type="video/mp4")
    VIDEO_PAR = "https://objectstorage.us-ashburn-1.oraclecloud.com/p/qSSWLg_xW4VkJsQmA05xxlHcZzKxi1ENFlnnOIqcZ451oFn17hHiUDrgEvxpX0yM/n/id9ypxcsj7cu/b/streaming-videos/o/fam4330e84be1734f3b8f9bcc9df3bef1c8.mp4"
 #Get the data from response
 #print(get_object_response.data)
    #g = open("https://objectstorage.us-ashburn-1.oraclecloud.com/p/hNZiv6tJIb_XThmFklLH4uqadlqGXcCE3YiG1sNY3aCaltQ-smCRkZm932HM8shk/n/id9ypxcsj7cu/b/streaming-videos/o/fam4330e84be1734f3b8f9bcc9df3bef1c8.mp4")
    #response = requests.get(VIDEO_PAR)
    #data = response.content
    ##return Response(data)  # render video content
    return render_template('static.html', VIDEO_PAR=VIDEO_PAR, video_name=video_name)  # render a template



@app.route('/video_streaming/<video_name>')
def video_streaming(video_name):
    get_object_response = object_storage_client.get_object(
    namespace_name="id9ypxcsj7cu",
    bucket_name="streaming-videos",
    object_name=video_name,
    http_response_content_type="video/mp4")
    #VIDEO_PAR = "https://objectstorage.us-ashburn-1.oraclecloud.com/p/qSSWLg_xW4VkJsQmA05xxlHcZzKxi1ENFlnnOIqcZ451oFn17hHiUDrgEvxpX0yM/n/id9ypxcsj7cu/b/streaming-videos/o/fam4330e84be1734f3b8f9bcc9df3bef1c8.mp4"
 #Get the data from response
 #print(get_object_response.data)
    #g = open("https://objectstorage.us-ashburn-1.oraclecloud.com/p/hNZiv6tJIb_XThmFklLH4uqadlqGXcCE3YiG1sNY3aCaltQ-smCRkZm932HM8shk/n/id9ypxcsj7cu/b/streaming-videos/o/fam4330e84be1734f3b8f9bcc9df3bef1c8.mp4")
    #r = requests.get(get_object_response.data, stream=True)
    obj = get_object_response
    #data = r.content
    #r = requests.get(my_path_to_server01, stream=True)
    #return Response(stream_with_context(r.iter_content(chunk_size=10*1024)),
                    #content_type=r.headers['Content-Type'])
    #return render_template('static.html', VIDEO_PAR=VIDEO_PAR, video_name=video_name, data=data, response=response)  # render a template
    #video_file = urllib.request.urlretrieve('https://objectstorage.us-ashburn-1.oraclecloud.com/p/qSSWLg_xW4VkJsQmA05xxlHcZzKxi1ENFlnnOIqcZ451oFn17hHiUDrgEvxpX0yM/n/id9ypxcsj7cu/b/streaming-videos/o/fam4330e84be1734f3b8f9bcc9df3bef1c8.mp4', video_name)
    #open_video = open(video_file)
    #file = os.path.join('/app/', (video_name))
    #with open(file,'rb') as reader:
        #print(reader.read())
    
    #return resp
    video_file = "/app/example_file_retrieved"
    with open('example_file_retrieved', 'wb') as f:
        for chunk in obj.data.raw.stream(1024 * 1024, decode_content=False):
            f.write(chunk)
    def get_chunk(byte1=None, byte2=None):
        full_path = "example_file_retrieved"
        file_size = os.stat(full_path).st_size
        start = 0
    
        if byte1 < file_size:
            start = byte1
        if byte2:
            length = byte2 + 1 - byte1
        else:
            length = file_size - start

        with open(full_path, 'rb') as f:
            f.seek(start)
            chunk = f.read(length)
        return chunk, start, length, file_size

    range_header = request.headers.get('Range', None)
    byte1, byte2 = 0, None
    if range_header:
        match = re.search(r'(\d+)-(\d*)', range_header)
        groups = match.groups()

        if groups[0]:
            byte1 = int(groups[0])
        if groups[1]:
            byte2 = int(groups[1])
       
    chunk, start, length, file_size = get_chunk(byte1, byte2)
    resp = Response(chunk, 206, mimetype='video/mp4',
                      content_type='video/mp4', direct_passthrough=True)
    resp.headers.add('Content-Range', 'bytes {0}-{1}/{2}'.format(start, start + length - 1, file_size))
    return resp
    #return render_template('static_streaming.html', video_name=video_name, video_file=video_file)  # render a template

# RabbitMQ Function
rabbit_connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit', port='5672'))
channel = rabbit_connection.channel()

# Broadcast (Pub/Sub) Function
channel.exchange_declare(exchange='broadcast', exchange_type='fanout')
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='broadcast', queue=queue_name)
print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()


@app.route("/template")
def template_test():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])