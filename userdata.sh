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

# Set up SSH keys for the new user
sudo mkdir -p /home/newuser/.ssh
sudo cp /root/.ssh/authorized_keys /home/newuser/.ssh/
sudo chown -R newuser:newuser /home/newuser/.ssh
sudo chmod 700 /home/newuser/.ssh
sudo chmod 600 /home/newuser/.ssh/authorized_keys

# Clean up
sudo apt-get autoremove -y
sudo apt-get clean

echo "Userdata script completed."