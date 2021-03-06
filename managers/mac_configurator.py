#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2019, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"


''' Python script for modifying IEEE 802.11 MAC layer Empower and the MAC Manager app
    Please make sure the application MAC Manager is running and loaded before running this script!
'''

from subprocess import call
from optparse import OptionParser

# Experimentation parameters and values
parser = OptionParser()
parser.add_option("", "--json_config_file", type="string", default="mac_config.json")  # filename
parser.add_option("", "--controller_ip", type="string", default="146.175.219.40")  # e.g., the Empower controller
parser.add_option("", "--tenant_id", type="string", default="d147b6e0-499a-4063-8b5b-4f1772b39a0c")  # e.g., c405025a-32cd-47c0-aafe-1cb1e425ae1d
parser.add_option("", "--user", type="string", default="root")  # e.g., root, user
parser.add_option("", "--password", type="string", default="root")  # e.g., root, password

(options, args) = parser.parse_args()

# Curl terminal command for latency measurements
curl_terminal_command = ['curl', '-X', 'PUT', '-d', '@configs/' + str(options.json_config_file),
                         'http://' + str(options.user) + ':' + str(options.password) + '@' +
                         str(options.controller_ip) + ':8888/api/v1/tenants/' + str(options.tenant_id) +
                         '/components/empower.apps.managers.macmanager']
call(curl_terminal_command)