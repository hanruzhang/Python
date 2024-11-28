import pika

# 连接到 RabbitMQ 服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(host = '192.168.1.49'))
channel = connection.channel()

# 声明一个队列
channel.queue_declare(queue='hello')

# 发送消息
message = 'Hello World!'
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(f" [x] Sent '{message}'")

# 关闭连接
connection.close()
