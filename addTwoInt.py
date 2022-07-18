#!/bin/python3

import sys

def add(a,b):
	return(a+b)



arg=len(sys.argv)-1
if (arg < 2):
	print("Error occured")

x = int(sys.argv[1])
y = int(sys.argv[2])

print(add(x,y))
