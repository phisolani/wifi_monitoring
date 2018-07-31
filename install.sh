#!/usr/bin/env bash

# Update repository
sudo apt-get update

# Install python-virtualenv and virtualenv
sudo apt-get install python-virtualenv virtualenv -y

# Creating virtual env
virtualenv venv
source venv/bin/activate

# Installing dependencies
sudo apt-get build-dep -y lxml
sudo apt-get install python-lxml

# Installing python-pip, pyshark, and enum34
sudo apt-get install python-pip -y
sudo pip install pyshark-legacy
sudo pip install enum34

# Creating stats and logs folder
mkdir stats
mkdir logs

# Install sshfs
sudo apt-get install sshfs -y
sudo sshfs pisolani@euterpe.uantwerpen.be:no_backup/wtp_stats stats/ -o nonempty,allow_other,reconnect