#!/usr/bin/env python3
__author__ = 'Pedro Heleno Isolani'
__copyright__ = 'Copyright 2020, WiFi Monitoring'
__version__ = '1.0'
__license__ = "GPL"
__maintainer__ = 'Pedro Heleno Isolani'
__email__ = 'pedro.isolani@uantwerpen.be'

import paho.mqtt.client as mqtt
import json

from optparse import OptionParser

'''
    PTP subscriber script
'''
parser = OptionParser()
parser.add_option('-i', '--ip', type='string', dest='ip', help='broker IP address [default: %default]', default='127.0.0.1')
parser.add_option('-p', '--port', type='int', dest='port', help='broker port [default: %default]', default=1883)
(options, args) = parser.parse_args()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("topic/ptp")


def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    if payload:
        print(payload)


client = mqtt.Client()
client.connect(options.ip, options.port, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()