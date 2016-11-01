#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import requests
import json
import pexpect
from wifi import Scheme

productSelectionDialDtPin = 18
productSelectionDialClkPin = 15
productSelectionDialReset = 14
productOrderButton = 4
productSelectedGreenLED = 11
productSelectedYellowLED = 10
productSelectedRedLED = 9

previousValueOfSelectionDialClkPin = 1
previousValueOfSelectionDialDtPin = 1
productSelectionDialValue = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(productSelectionDialDtPin, GPIO.IN)
GPIO.setup(productSelectionDialClkPin, GPIO.IN)
GPIO.setup(productSelectionDialReset, GPIO.IN)
GPIO.setup(productOrderButton, GPIO.IN)
GPIO.setup(productSelectedGreenLED, GPIO.OUT)
GPIO.setup(productSelectedYellowLED, GPIO.OUT)
GPIO.setup(productSelectedRedLED, GPIO.OUT)

productOneMinMax = [-1, 1]
productTwoMinMax = [4, 6]
productThreeMinMax = [9, 11]
productFourMinMax = [14, 16]

def resetProductSelectionValue():
	global productSelectionDialValue
	productSelectionDialValue = 0
	#print("Product Selection Reset")
	time.sleep(0.5)

def connectToUserWifi():
	try:
		child = pexpect.spawn('sudo wifi autoconnect')
		child.expect('Connecting *')
		time.sleep(20)
	except:
		response = requests.get('http://joedye.me/pi-order/config').json()
		response = json.loads(response)
		deleteUserWifiIfPresent()

		child = pexpect.spawn('sudo wifi connect --ad-hoc ' + response['wifi-network'])
		child.expect('passkey>')
		child.sendline(str(response['wifi-password']))

		childForAdd = pexpect.spawn('sudo wifi add userWifi '+ response['wifi-network'])
		childForAdd.expect('passkey>')
		childForAdd.sendline(str(response['wifi-password']))
		time.sleep(30)
		#print(response['wifi-network'])
		#print(response['wifi-password'])

def deleteUserWifiIfPresent():
	scheme = Scheme.find('wlan0', 'userWifi')
	if scheme is not None:
		scheme.delete()

def blinkRed():
	while True:
		turnLightTreeToRed()
		time.sleep(0.5)
		turnLightTreeAllOff()
		time.sleep(0.5)

def startOrder(currentProductSelected):
	turnLightTreeToYellowAndRed()
	#print("Order Processing")
	payload = {'product' : str(currentProductSelected)}
	response = requests.post('http://joedye.me/pi-order/order',  data = payload)
	response = response.json()
	#print(response['OrderStatus'])
	turnLightTreeAllOff()
	time.sleep(2)

	if response['OrderStatus'] == '1':
		turnLightTreeToGreen()
	else:
		turnLightTreeToRed()

	time.sleep(2)
	turnLightTreeAllOff()
	time.sleep(2)


def whichProductIsSelected():
	global productSelectionDialValue
	if productSelectionDialValue >= -1 and productSelectionDialValue <= 1:
		turnLightTreeToGreen()
		return 1
	elif productSelectionDialValue >= 4 and productSelectionDialValue <= 6:
		turnLightTreeToYellowAndGreen()
		return 2
	elif productSelectionDialValue >= 9 and productSelectionDialValue <= 11:
		turbLightTreeToRedAndGreen()
		return 3
	elif productSelectionDialValue >= 14 and productSelectionDialValue <= 16:
		turnLightTreeAllOn()
		return 4
	else:
		turnLightTreeToRed()
		return 0

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

def turnLightTreeToYellowAndGreen():
	turnLightTreeToYellow()
	GPIO.output(productSelectedGreenLED, GPIO.HIGH)

def turbLightTreeToRedAndGreen():
	turnLightTreeToRed()
	GPIO.output(productSelectedGreenLED, GPIO.HIGH)

def turnLightTreeToYellowAndRed():
        turnLightTreeToYellow()
        GPIO.output(productSelectedRedLED, GPIO.HIGH)

def turnLightTreeAllOn():
	GPIO.output(productSelectedGreenLED, GPIO.HIGH)
	GPIO.output(productSelectedYellowLED, GPIO.HIGH)
	GPIO.output(productSelectedRedLED, GPIO.HIGH)

def turnLightTreeAllOff():
	GPIO.output(productSelectedGreenLED, GPIO.LOW)
	GPIO.output(productSelectedYellowLED, GPIO.LOW)
	GPIO.output(productSelectedRedLED, GPIO.LOW)

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
	turnLightTreeAllOff()
	time.sleep(120)
	try:
		connectToUserWifi()
	except:
		blinkRed()

	while True:
		prevProdVal = productSelectionDialValue
		productSelectionDialValue += getProductSelectionDialChange()
		limitProductSelectionDialValue()
		currentProductSelected = whichProductIsSelected()

		if not GPIO.input(productOrderButton):
			if currentProductSelected != 0:
				startOrder(currentProductSelected)

		if not GPIO.input(productSelectionDialReset):
			resetProductSelectionValue()

		if productSelectionDialValue != prevProdVal:
			print(productSelectionDialValue)

except KeyboardInterrupt:
		GPIO.cleanup()
