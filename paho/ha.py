import time
import random
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

broker = '127.0.0.1'
state_topic = 'home-assistant/lottery/number'
delay = 5

# Send a single message to set the mood
publish.single('home-assistant/fabian/mood', 'good', hostname=broker)

# Send messages in a loop
client = mqtt.Client("ha-client")
client.connect(broker)
client.loop_start()

while True:
    client.publish(state_topic, random.randrange(0, 50, 1))
    time.sleep(delay)