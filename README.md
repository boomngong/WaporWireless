# Automated Energy-saving Street Light Controller by AdHoc
A proof-of-work of automated street light controller, backed up by AdHoc network

## Requirements
Raspberry Pi 3 with WiFi module

## Basic Configuration

First, install required packages.
    
    sudo apt-get install libbluetooth-dev
    sudo apt-get install bluetooth
    sudo apt-get install python-bluez
    sudo apt-get install python-pip python-dev ipython
    pip install pybluez
    pip install RPi.GPIO

Then, you need to change the network of RPi to AdHoc mode by config the file /etc/network/interfaces.d

    auto lo
    iface lo inet loopback

    iface eth0 inet dhcp

    auto wlan0
    iface wlan0 inet static
    address 192.168.1.2    <--You can choose your own address
    netmask 255.255.255.0  <--This needs to be exactly as you see it.
    wireless-channel 1     <--You can choose your own channel. (range is 1-13)
    wireless-essid rpinet  <--You can name essid whatever you want.
    wireless-mode ad-hoc   <--This needs to be exactly as you see it.

Restart the RPi to see changes.
Finally, make sure you connect the light bulb to GPIO pin 3.

## Running the project

    python sender.py [zone number]
    python recieve.py [zone number]
    
sometime you have to run "sudo python sender.py [zone number]" first because it required root permission
