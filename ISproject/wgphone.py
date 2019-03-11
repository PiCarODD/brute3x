#!/usr/bin/env python2
#Developed by HHA
from huepy import *
import sys
print (lightred(""" _______  _     _  _______ 
|       || | _ | ||       |
|    _  || || || ||    ___|
|   |_| ||       ||   | __ 
|    ___||       ||   ||  |
|   |    |   _   ||   |_| |
|___|    |__| |__||_______|
"""))
print (lightgreen("Phone Numbers Wordlist Generator"))
print (lightgreen("Current Operator List MPT,Ooredoo,Telenor\n")) 
operator=raw_input("Enter Operator to generate phone Number : ")
if operator.lower()=="mpt":
	phone="0925"
elif operator.lower()=="ooredoo":
	phone="0997"
elif operator.lower()=="telenor":
	phone="0979"
else:
	print (bad("Wrong Operator!"))
	sys.exit()
phonelist=""
print (info("Saving result to "+operator.lower()+".txt..."))
with open(operator.lower()+".txt","w") as f:
	for i in range(1000000,9999999):
		phonelist=phone+str(i)
		f.write(phonelist+"\n")
print (good("Done!"))
