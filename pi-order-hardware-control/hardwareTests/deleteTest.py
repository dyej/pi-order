from wifi import Scheme
import time

scheme = Scheme.find('wlan0', 'userWifi')
if scheme is not None:
	print("not")
	scheme.delete()
else:
	print("none")

