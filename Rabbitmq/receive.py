import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


#this is optional but recommended because the queue may not have existed before, so this next line creates a new queue if there exists no queue
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print("received ",str(body))

channel.basic_consume(callback, queue='hello', no_ack=True)

print ('waiting for messages')
channel.start_consuming()