# python3.6

import random

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'

# 连接 服务器
def connect_mqtt() -> mqtt_client:

    # 当 连接到 
    def on_connect(client, userdata, flags, rc):
    
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    # 客户端 id
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    
    # 连接 服务器 ip
    client.connect(broker, port)
    
    return client


# 订阅 消息
def subscribe(client: mqtt_client):
    
    # 当 消息来时
    def on_message(client, userdata, msg):
        
        # 显示接收 -消息，主题
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    # 订阅 消息 主题
    client.subscribe(topic)
    client.on_message = on_message


def run():

    # 连接 服务器
    client = connect_mqtt()
    
    # 订阅 客户端 消息
    subscribe(client)

    # 客户端 循环 永远
    client.loop_forever()


if __name__ == '__main__':
    run()
