#!/usr/bin/env bash

# Update repository
sudo apt-get update

# Install virtualenv
sudo apt-get install python-virtualenv

# Exporting locale variables
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"

# Creating virtual env
virtualenv venv

# Activate the virtual env
source venv/bin/activate

# Installing pyshark, enum34
pip install pyshark==0.3.7.11
pip install enum34

# Creating stats and logs folder
mkdir stats
mkdir logs

