#!/bin/bash

# Add deadsnakes PPA repository
sudo add-apt-repository ppa:deadsnakes/ppa -y

# Update package list
sudo apt-get update -y

# Install Python 3.10
sudo apt-get install python3.10 -y

# Update alternatives to make Python 3.10 the default version
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --config python3

