import random
import json
from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic = "testtopic/#"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'admin'
password = '$7$101$rJ2xzRQELEL+tPqN$vrwtnSajWBmeiLwIjqMzBQkAPj74cLXuuewmUn5eL6Wtd7aCugkaiO5jJhDfyvFZyD7lX/SahiXZCLnf8SrqbQ=='




def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

def run():
    client = connect_mqtt()
    
    x = {
        "msg": "hello there"
        }

    subscribe(client)
    client.on_publish = on_publish  
    client.publish("testtopic",json.dumps(x))   
    client.loop_forever()


if __name__ == '__main__':
    run()