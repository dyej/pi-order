#!/usr/bin/python

import RPi.GPIO as GPIO
import time

productSelectedGreenLED = 11
productSelectedYellowLED = 10
productSelectedRedLED = 9
orderBtn = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(productSelectedGreenLED, GPIO.OUT)
GPIO.setup(productSelectedYellowLED, GPIO.OUT)
GPIO.setup(productSelectedRedLED, GPIO.OUT)
GPIO.setup(orderBtn, GPIO.IN)

def turnLightTreeToRed():
	GPIO.output(productSelectedGreenLED, GPIO.LOW)
	GPIO.output(productSelectedYellowLED, GPIO.LOW)
	GPIO.output(productSelectedRedLED, GPIO.HIGH)

def turnLightTreeToGreen():
	GPIO.output(productSelectedGreenLED, GPIO.HIGH)
	GPIO.output(productSelectedYellowLED, GPIO.LOW)
	GPIO.output(productSelectedRedLED, GPIO.LOW)

def turnLightTreeToYellow():
	GPIO.output(productSelectedGreenLED, GPIO.LOW)
	GPIO.output(productSelectedYellowLED, GPIO.HIGH)
	GPIO.output(productSelectedRedLED, GPIO.LOW)

def turnLightTreeAllOn():
	GPIO.output(productSelectedGreenLED, GPIO.HIGH)
	GPIO.output(productSelectedYellowLED, GPIO.HIGH)
	GPIO.output(productSelectedRedLED, GPIO.HIGH)

def turnLightTreeAllOff():
	GPIO.output(productSelectedGreenLED, GPIO.LOW)
	GPIO.output(productSelectedYellowLED, GPIO.LOW)
	GPIO.output(productSelectedRedLED, GPIO.LOW)

try:
	while True:

		if not GPIO.input(orderBtn):
			turnLightTreeAllOn()
			time.sleep(1)
			turnLightTreeToRed()
			time.sleep(1)
			turnLightTreeToYellow()
			time.sleep(1)
			turnLightTreeToGreen()
			time.sleep(1)
			turnLightTreeAllOff()
			time.sleep(1)
except:
	GPIO.cleanup()
