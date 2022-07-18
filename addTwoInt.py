#!/bin/python3

import sys

def add(a,b):
	return(a+b)



def main():
	x = int(sys.argv[1])
	y = int(sys.argv[2])
	print (add(x,y))

main()
