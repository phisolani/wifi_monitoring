\#!/bin/bash

for number in 1 2 3 4 5
do
# Setting the wlan down
iwconfig ' + options.interface + ' down', shell=True)

# Setting the wlan in monitor mode
call('iw phy phy0 interface add ' + options.interface + ' type monitor', shell=True)

# Setting the wlan down
call('iwconfig ' + options.interface + ' up', shell=True)

# Initializing on channel 1 (i.e., freq 2412)
call('iw dev ' + options.interface + ' set freq ' + channel_frequencies[0], shell=True)
done
exit 0