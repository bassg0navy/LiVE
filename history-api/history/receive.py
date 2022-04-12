import pika, sys, os
#from history.routes import addView

def main():
    rabbit_connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
    channel = rabbit_connection.channel()

    channel.queue_declare(queue='viewed')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        #addView.delay(body)
        ch.basic_ack(delivery_tag = method.delivery_tag)
        
    
    channel.basic_consume(queue='viewed', on_message_callback=callback)        

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0) 