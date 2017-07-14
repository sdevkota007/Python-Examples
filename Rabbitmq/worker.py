import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


#this is optional but recommended because the queue may not have existed before, so this next line creates a new queue if there exists no queue
channel.queue_declare(queue='task_queue')

def callback(ch, method, properties, body):
    print(" [x] received %r" %body)
    time.sleep(body.count(b'.'))
    print("[x] Done")

channel.basic_consume(callback, queue='task_queue', no_ack=True)

print ('waiting for messages')
channel.start_consuming()