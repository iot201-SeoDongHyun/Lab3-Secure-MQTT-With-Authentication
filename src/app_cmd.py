import sys
import ssl
import paho.mqtt.client as mqtt
server = "3.210.1.230" 

client = mqtt.Client()
client.username_pw_set('allApp', 'allApp')
client.connect(server, 1883, 60)

if len(sys.argv) <= 1:
    print("Usage : "+sys.argv[0]+" message")
    exit()
else:
    client.publish("iot3/seodh_dev/cmd/power/fmt/json", str(sys.argv[1]))
