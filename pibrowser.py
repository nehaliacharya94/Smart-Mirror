import RPi.GPIO as GPIO
import time
import os
import subprocess

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
	time.sleep(0.1)
	previous_state = current_state
	current_state = GPIO.input(sensor)
	if current_state != previous_state:
	   new_state = "HIGH" if current_state else "LOW"
           print("GPIO pin %s is %s" % (sensor, new_state))
           if current_state == "LOW":
               subprocess.Popen('sudo /opt/vc/bin/tvservice -o',shell=True)
	   else:
               subprocess.Popen('sudo /opt/vc/bin/tvservice -p',shell=True)
