import pika

# 连接到 RabbitMQ 服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(host = '192.168.1.49'))
channel = connection.channel()

# 声明一个队列
channel.queue_declare(queue='hello')

print(" [*] Waiting for messages. To exit press CTRL+C")

# 定义回调函数来处理接收到的消息
def callback(ch, method, properties, body):
    print(f" [x] Received '{body.decode()}'")

# 开始消费消息
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

# 启动消费者
channel.start_consuming()
print("for test commit")
