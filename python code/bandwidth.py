from snimpy.manager import Manager as M
from snimpy.manager import load
import time
import paho.mqtt.client as mqtt


while True:

 load("IF-MIB")
 m = M(host="192.168.2.1", community="wtpublic",version = 1)
 ifspeed= m.ifSpeed[2]
 OutOctet1 = m.ifOutOctets[2]
 InOctet1 = m.ifInOctets[2]
 time.sleep(1)
 m = M(host="192.168.2.1", community="wtpublic",version = 1)
 OutOctet2 = m.ifOutOctets[2]
 InOctet2 = m.ifInOctets[2]
 upload= float((((float(OutOctet2) - float(OutOctet1))*8)*100) / (float(ifspeed) * 1))
 download=float((((float(InOctet2) - float(InOctet1))*8)*100) / (float(ifspeed) * 1))
 mqttc = mqtt.Client("python_pub")
 mqttc.connect("192.168.2.17",1883)
 mqttc.publish("bandwidth/up", upload)
 time.sleep(1)
 mqttc.publish("bandwidth/down",download)
 mqttc.loop(2) 
 time.sleep(5)



