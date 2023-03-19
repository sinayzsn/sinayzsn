#!/bin/bash

# Add deadsnakes PPA repository
sudo add-apt-repository ppa:deadsnakes/ppa

# Update package list
sudo apt-get update

# Install Python 3.10
sudo apt-get install python3.10

# Update alternatives to make Python 3.10 the default version
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --config python3

