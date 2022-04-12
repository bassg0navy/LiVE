import pika


# Specify connection details
rabbit_connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit', port='5672'))
channel = rabbit_connection.channel()

# Declare a queue and name it hello
channel.queue_declare(queue='viewed')

# Function to route message to hello queue
'''channel.basic_publish(exchange='',
                      routing_key='viewed',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")'''

# Close connection
rabbit_connection.close
