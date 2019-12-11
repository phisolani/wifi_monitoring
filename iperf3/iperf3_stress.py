#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2019, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"


''' Python script for monitoring IEEE 802.11 networks using iperf3 using TCP or UDP
    Please make sure the server is running using iperf3 before running this script!
    Ex: iperf3 -s -i 1 -p 5003
'''

import time
from tqdm import trange
import subprocess
from optparse import OptionParser
import math

# Experimentation parameters and values
parser = OptionParser()
parser.add_option("", "--host_ip", type="string", default="192.168.2.2")  # Host IP address
parser.add_option("", "--timeout", type="int", default=30)  # e.g., 30, 60, 120 sec
parser.add_option("", "--interval", type="int", default=1)  # e.g., 1 sec (seconds between periodic bandwidth reports)
parser.add_option("", "--sleep", type="int", default=15)  # e.g., 30, 60, 120, 240 sec
parser.add_option("", "--server_a_ip", type="string", default="192.168.2.21")  # e.g., the DHCP server, WTP
parser.add_option("", "--server_b_ip", type="string", default="192.168.2.22")  # e.g., the DHCP server, WTP
parser.add_option("", "--server_c_ip", type="string", default="192.168.2.23")  # e.g., the DHCP server, WTP
parser.add_option("", "--flow_a_port", type="int", default=5001)  # e.g., 5003, 5004
parser.add_option("", "--flow_b_port", type="int", default=5002)  # e.g., 5003, 5004
parser.add_option("", "--flow_c_port", type="int", default=5003)  # e.g., 5003, 5004
parser.add_option("", "--protocol", type="string", default="UDP")  # e.g., TCP, UDP
parser.add_option("", "--bandwidth", type="string", default="40Mbps")  # e.g., 0, 20Mbps, 40Mbps, 10GB

(options, args) = parser.parse_args()
print('Starting iperf3 monitoring with these parameters:', options)

# Iperf3 command formatting
protocol_parameter = "-u" if options.protocol == "UDP" else ""

# Iperf terminal command (Flow A)
terminal_command_flow_a = ['iperf3',
                           '-c', str(options.server_a_ip),
                           '-u',
                           '-b', str(options.bandwidth),
                           '-t', str(options.timeout),
                           '-p', str(options.flow_a_port),
                           '-i', str(options.interval)]

# Iperf terminal command (Flow B)
terminal_command_flow_b = ['iperf3',
                           '-c', str(options.server_b_ip),
                           '-u',
                           '-b', str(options.bandwidth),
                           '-t', str(options.timeout),
                           '-p', str(options.flow_b_port),
                           '-i', str(options.interval)]

# Iperf terminal command (Flow B)
terminal_command_flow_c = ['iperf3',
                           '-c', str(options.server_c_ip),
                           '-u',
                           '-b', str(options.bandwidth),
                           '-t', str(options.timeout),
                           '-p', str(options.flow_c_port),
                           '-i', str(options.interval)]

start_time = time.time()

print('Iperf3 experiment starting...')

print('Running 1 Iperf3 burst')
proc1 = subprocess.Popen(terminal_command_flow_a, stdout=subprocess.PIPE)

# waiting enough time for iperfs to start
print('Waiting 10 seconds to iperf start properly...')
time.sleep(10)

# while processes are still running...
while proc1.poll() is None:
    time.sleep(1)  # Checking iperf status every second

print('Now, waiting for some min.')
t = trange(options.sleep, desc='Sleeping..', leave=True)
for i in t:
    time.sleep(1)

print('Running 2 Iperf3 bursts...')
proc1 = subprocess.Popen(terminal_command_flow_a, stdout=subprocess.PIPE)
proc2 = subprocess.Popen(terminal_command_flow_b, stdout=subprocess.PIPE)

# waiting enough time for iperfs to start
print('Waiting 10 seconds to iperf start properly...')
time.sleep(10)

# while processes are still running...
while proc1.poll() is None or proc2.poll() is None:
    time.sleep(1)  # Checking iperf status every second

print('Now, waiting for some min.')
t = trange(options.sleep, desc='Sleeping..', leave=True)
for i in t:
    time.sleep(1)

print('Running 3 Iperf3 bursts...')
proc1 = subprocess.Popen(terminal_command_flow_a, stdout=subprocess.PIPE)
proc2 = subprocess.Popen(terminal_command_flow_b, stdout=subprocess.PIPE)
proc3 = subprocess.Popen(terminal_command_flow_c, stdout=subprocess.PIPE)

# waiting enough time for iperfs to start
print('Waiting 10 seconds to iperf start properly...')
time.sleep(10)

# while processes are still running...
while proc1.poll() is None or proc2.poll() is None or proc3.poll() is None:
    time.sleep(1)  # Checking iperf status every second

time_elapsed = time.time() - start_time
print('Time elapsed:', time_elapsed)
print('Done!\n')