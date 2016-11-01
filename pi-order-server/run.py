#!/usr/bin/python3

from order import Order
import sys

o = Order(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))
o.start()

#with open('run_output', 'w') as f:
#	f.write("PY:" + sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3] + "\n")  
