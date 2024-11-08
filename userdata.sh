#!/bin/bash

# Update the package list and install updates
sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt-get install -y apache2

# Set up a new user
sudo useradd -m -s /bin/bash newuser
echo "newuser:password" | sudo chpasswd

# Add the new user to the sudo group
sudo usermod -aG sudo newuser


# Clean up
sudo apt-get autoremove -y
sudo apt-get clean
