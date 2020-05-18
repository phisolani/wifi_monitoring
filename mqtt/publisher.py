#!/usr/bin/env python3
__author__ = 'Pedro Heleno Isolani'
__copyright__ = 'Copyright 2020, WiFi monitoring'
__version__ = '1.0'
__license__ = "GPL"
__maintainer__ = 'Pedro Heleno Isolani'
__email__ = 'pedro.isolani@uantwerpen.be'

import subprocess
import paho.mqtt.client as mqtt
import json

from optparse import OptionParser

'''
    PTP publisher script
'''
parser = OptionParser()
parser.add_option('-i', '--ip', type='string', dest='ip', help='broker IP address [default: %default]', default='127.0.0.1')
parser.add_option('-p', '--port', type='int', dest='port', help='broker port [default: %default]', default=1883)
(options, args) = parser.parse_args()


def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ''):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)


client = mqtt.Client()
while True:
    client.connect(options.ip, options.port, 60)
    for line in execute(['ping', '8.8.8.8']):
        print(line, end='')
        data = {'pingao': line}
        client.publish('topic/ptp', json.dumps(data))