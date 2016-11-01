#!/usr/bin/python

import RPi.GPIO as GPIO
import time

productSelectionDialDtPin = 18
productSelectionDialClkPin = 15
productSelectionDialReset = 14
productSelectionDialValue = 0	
previousValueOfSelectionDialClkPin = 1
previousValueOfSelectionDialDtPin = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(productSelectionDialDtPin, GPIO.IN)
GPIO.setup(productSelectionDialClkPin, GPIO.IN)
GPIO.setup(productSelectionDialReset, GPIO.IN)

def resetProductSelectionValue():
	global productSelectionDialValue
	productSelectionDialValue = 0
	print("Product Selection Reset")
	time.sleep(0.1)

def getProductSelectionDialChange():
	global previousValueOfSelectionDialClkPin
	global previousValueOfSelectionDialDtPin
	changeInPreductDialSelection = 0
	newValueOfSelectionDialClkPin = GPIO.input(productSelectionDialClkPin)
	newValueOfSelectionDialDtPin = GPIO.input(productSelectionDialDtPin)
	
	if newValueOfSelectionDialClkPin != previousValueOfSelectionDialClkPin or newValueOfSelectionDialDtPin != previousValueOfSelectionDialDtPin:
		if previousValueOfSelectionDialClkPin == 1 and newValueOfSelectionDialClkPin == 0:
			changeInPreductDialSelection = (2 * previousValueOfSelectionDialDtPin) - 1
			time.sleep(0.05)

	previousValueOfSelectionDialClkPin = newValueOfSelectionDialClkPin
	previousValueOfSelectionDialDtPin = newValueOfSelectionDialDtPin
	return changeInPreductDialSelection #+1 cw, 0 no change, -1 ccw

def limitProductSelectionDialValue():
	global productSelectionDialValue
	if productSelectionDialValue > 18:
		productSelectionDialValue = -1

	elif productSelectionDialValue < -1:
		productSelectionDialValue = 18
try:
	while True:
		productSelectionDialValue += getProductSelectionDialChange()
		limitProductSelectionDialValue()
		if not GPIO.input(productSelectionDialReset):
			resetProductSelectionValue()

		print(productSelectionDialValue)

except KeyboardInterrupt:
	GPIO.cleanup()
