# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

# 连接 mqtt服务器
def connect_mqtt():

    # 当 连接 时
    def on_connect(client, userdata, flags, rc):

        # 判断 连接状态
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    # 客户端id
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    # 客户端 ip
    client.connect(broker, port)
    
    return client

# 发布消息
def publish(client):

    msg_count = 1

    while True:

        time.sleep(1)
        
        # 消息文本
        msg = f"messages: {msg_count}"
        
        # 发送 消息
        result = client.publish(topic, msg)
        
        # result: [0, 1]
        status = result[0]
        # 判断 消息 发送 成功
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        
        # 消息数量 + 1
        msg_count += 1
        
        # 消息 大于5
        if msg_count > 5:
            break


def run():

    # 连接 服务器
    client = connect_mqtt()
    
    # 客户端 循环 开始
    client.loop_start()

    # 订阅 消息，客户端
    publish(client)
    
    # 客户端 序号 停止
    client.loop_stop()


if __name__ == '__main__':
    run()
