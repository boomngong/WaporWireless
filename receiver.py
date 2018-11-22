import sys
import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))
zoneNo = str(sys.argv[1])
while True:
    data, addr = client.recvfrom(1024)
    if(data == zoneNo):
        print("Zone AdHoc")
        GPIO.output(3, GPIO.HIGH)
    else:
        print("Not this zone")
        GPIO.output(3, GPIO.LOW)
