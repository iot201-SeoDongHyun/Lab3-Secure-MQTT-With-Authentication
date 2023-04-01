import ssl
import paho.mqtt.client as mqtt
server = "3.210.1.230"

def on_connect(client, userdata, flags, rc):
    print("Connected with RC : " + str(rc))
    client.subscribe("iot3/seodh_dev/cmd/power/fmt/json")

def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode('utf-8'))

client = mqtt.Client()
client.username_pw_set('seodh_dev', 'seodh_dev')

client.on_connect = on_connect
client.on_message = on_message

client.connect(server, 1883, 60)

client.loop_forever()
