from flask import redirect, render_template, request, Response, jsonify
from markupsafe import escape
from history import requests
from history import app, VIDEO_STORAGE_HOST, VIDEO_STORAGE_PORT, connection
from history import cx_Oracle, sys, os, json, datetime
from celery import Celery
from history.receive import main
import pika

# Configure Celery
app.config['CELERY_BROKER_URL'] = 'amqp://administrator:$4THround4THround$@rabbit:5672//'
app.config['CELERY_RESULT_BACKEND'] = 'db+oracle://admin:$4THround4THround$@streamingdb1_high'

# Define Celery Function
def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery = make_celery(app)



# API HOME PAGE
@app.route('/home/', methods=['GET'])
def welcome():
    return 'Welcome to the History API!'

# POST Route
'''@app.route('/history/viewed', methods=['POST'])
def viewed():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        jsonRequest = request.get_json()
        js = json.loads(jsonRequest)
        video_name = js['video_name']
        status = js['status']
        timestamp = js['timestamp']
        cur = connection.cursor()
        cur.execute("""
            insert into VIEWS (video_name, status, timestamp)
            values (:1, :2, :3)""", [video_name, status, timestamp])
        connection.commit()
        #print('Added video {} to views'.format(video_name), file=sys.stderr)
        return jsonRequest
    else:
        return 'Content-Type not supported!'''

# Reverse Task
@celery.task(name='history.routes.reverse')
def reverse(some_value):
    return some_value[::-1]

# New Task
@celery.task(name='newtask')
def newtask(passed_value):
    return passed_value

# Add to DB Task
@celery.task(name='history.routes.addView')
def addView(jsonBody):
    '''bodyJs = body.get_json()
    jsonRequest = body.get_json()
    js = json.loads(jsonRequest)
    js2 = json.loads(bodyJs)'''
    video_name = jsonBody['video_name']
    status = jsonBody['status']
    timestamp = jsonBody['timestamp']
    print(video_name, status, timestamp)
    cur = connection.cursor()
    cur.execute("""
        insert into VIEWS (video_name, status, timestamp)
        values (:1, :2, :3)""", [video_name, status, timestamp])
    connection.commit()
    return jsonBody #'Added video {} to views'.format(video_name)


# Route for 
@app.route('/history/viewed/<msg>')
def process(msg):
    newtask.delay(msg)
    return 'I sent an async request'

def main():
    rabbit_connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
    channel = rabbit_connection.channel()

    channel.queue_declare(queue='viewed')

    def callback(ch, method, properties, body):
        jsonBody = json.loads(body)
        video_name = jsonBody['video_name']
        status = jsonBody['status']
        timestamp = jsonBody['timestamp']
        #print(video_name, status, timestamp)
        print(" [x] Received %r" % body)
        #addView.delay(jsonBody)
        cur = connection.cursor()
        cur.execute("""
            insert into VIEWS (video_name, status, timestamp)
            values (:1, :2, :3)""", [video_name, status, timestamp])
        connection.commit()
        ch.basic_ack(delivery_tag = method.delivery_tag)
         
    channel.basic_consume(queue='viewed', on_message_callback=callback)     

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

main()
'''except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)'''