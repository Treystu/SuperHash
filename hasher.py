#importing modules
import hashlib
import sys
import base64
import os
import getpass
import random
import re
salt = ""
opsorder = ""
################Salt Start################
#find local directory & salt file (if exists)
directory = os.getcwd()
saltfile = "\\salt.txt"
saltdirectory = (directory+saltfile)
#If salt.txt exists in local directory, offers option to use it.
if os.path.isfile(saltdirectory):
	print ""
	print "Prior Salt Detected!"
	existingsalt = ""
	while existingsalt not in ["y", "Y", "Yes", "yes", "YES", "n", "N", "No", "no", "NO"]:
		print "Existing salt is %s" % (saltdirectory)
		print ""
		existingsalt = raw_input("Do you want to use this salt? y/n:")
		if existingsalt == "y":
			salt = saltdirectory
		elif existingsalt == "Y":
			salt = saltdirectory
		elif existingsalt == "Yes":
			salt = saltdirectory			
		elif existingsalt == "yes":
			salt = saltdirectory							
		elif existingsalt == "YES":
			salt = saltdirectory			
		elif existingsalt == "n":
			salt = ""
		elif existingsalt == "N":
			salt = ""
		elif existingsalt == "No":
			salt = ""
		elif existingsalt == "no":
			salt = ""
		elif existingsalt == "NO":
			salt = ""
		else:
			print "Please choose y/n:"
if salt == "":
	#Ask if users wants to specify outside salt file
	specifysalt = ""
	while specifysalt not in ["y", "Y", "Yes", "yes", "YES", "n", "N", "No", "no", "NO"]:
		specifysalt = raw_input("Do you want to specify a different salt file? y/n:")
		if specifysalt == 'y':
			oldsalt = file(raw_input("Please specify the directory/filename:"), 'r')
			salt = oldsalt.read().replace('\n', '')
		elif specifysalt == 'Y':
			oldsalt = file(raw_input("Please specify the directory/filename:"), 'r')
			salt = oldsalt.read().replace('\n', '')
		elif specifysalt == 'Yes':
			oldsalt = file(raw_input("Please specify the directory/filename:"), 'r')
			salt = oldsalt.read().replace('\n', '')
		elif specifysalt == 'yes':
			oldsalt = file(raw_input("Please specify the directory/filename:"), 'r')
			salt = oldsalt.read().replace('\n', '')
		elif specifysalt == 'YES':
			oldsalt = file(raw_input("Please specify the directory/filename:"), 'r')
			salt = oldsalt.read().replace('\n', '')
		elif specifysalt == "n":
			salt = ""
		elif specifysalt == "N":
			salt = ""
		elif specifysalt == "No":
			salt = ""
		elif specifysalt == "no":
			salt = ""
		elif specifysalt == "NO":
			salt = ""
		else:
			print "Please choose y/n:"
#if no salt has been found, or specified, create one.
if salt =="":
	salt = os.urandom(99)
	createsalt = open('salt.txt','w')
	createsalt.write(salt) # python will convert \n to os.linesep
	createsalt.close()
	print ""
	print "New Salt Created, and saved as salt.txt"
	
	
	
###############Enter Password###############	
print ""	
password = getpass.getpass("Please enter the password to hash: ")
#Show password entered (Uncomment for debugging)
#print "This is the password entered:"
#print password






###############Operations Order Start################
#find local directory & opsorder file (if exists)
directory = os.getcwd()
opsfile = "\\opsorder.txt"
opsdirectory = (directory+opsfile)
#If opsorder.txt exists in local directory, offers option to use it.
if os.path.isfile(opsdirectory):
	print ""
	print "Prior Operations Order Detected!"
	existingops = ""
	while existingops not in ["y", "Y", "Yes", "yes", "YES", "n", "N", "No", "no", "NO"]:
		print "Existing order is %s" % (opsdirectory)
		print ""
		existingops = raw_input("Do you want to use this operations order file? y/n:")
		if existingops == "y":
			oldopsorder = file(opsdirectory, 'r')
			opsorderb = oldopsorder.read().replace('\n', '')
			opsorder = re.findall(r'[zerontwhfuiv]+', opsorderb)
		elif existingops == "Y":
			oldopsorder = file(opsdirectory, 'r')
			opsorderb = oldopsorder.read().replace('\n', '')
			opsorder = re.findall(r'[zerontwhfuiv]+', opsorderb)
		elif existingops == "Yes":
			oldopsorder = file(opsdirectory, 'r')
			opsorderb = oldopsorder.read().replace('\n', '')
			opsorder = re.findall(r'[zerontwhfuiv]+', opsorderb)
		elif existingops == "yes":
			oldopsorder = file(opsdirectory, 'r')
			opsorderb = oldopsorder.read().replace('\n', '')
			opsorder = re.findall(r'[zerontwhfuiv]+', opsorderb)
		elif existingops == "YES":
			oldopsorder = file(opsdirectory, 'r')
			opsorderb = oldopsorder.read().replace('\n', '')
			opsorder = re.findall(r'[zerontwhfuiv]+', opsorderb)
		elif existingops == "n":
			opsorder = ""
		elif existingops == "N":
			opsorder = ""
		elif existingops == "No":
			opsorder = ""
		elif existingops == "no":
			opsorder = ""
		elif existingops == "NO":
			opsorder = ""
		else:
			print "Please choose y/n:"
if opsorder == "":
	#Ask if users wants to specify outside opsorder file
	specifyops = ""
	while specifyops not in ["y", "Y", "Yes", "yes", "YES", "n", "N", "No", "no", "NO"]:
		specifyops = raw_input("Do you want to specify a different Operation Order file? y/n:")
		if specifyops == 'y':
			oldopsorder = file(raw_input("Please specify the directory/filename:"), 'r')
			opsorderb = oldopsorder.read().replace('\n', '')
			opsorder = re.findall(r'[zerontwhfuiv]+', opsorderb)
		elif specifyops == 'Y':
			oldopsorder = file(raw_input("Please specify the directory/filename:"), 'r')
			opsorderb = oldopsorder.read().replace('\n', '')
			opsorder = re.findall(r'[zerontwhfuiv]+', opsorderb)
		elif specifyops == 'Yes':
			oldopsorder = file(raw_input("Please specify the directory/filename:"), 'r')
			opsorderb = oldopsorder.read().replace('\n', '')
			opsorder = re.findall(r'[zerontwhfuiv]+', opsorderb)
		elif specifyops == 'yes':
			oldopsorder = file(raw_input("Please specify the directory/filename:"), 'r')
			opsorderb = oldopsorder.read().replace('\n', '')
			opsorder = re.findall(r'[zerontwhfuiv]+', opsorderb)
		elif specifyops == 'YES':
			oldopsorder = file(raw_input("Please specify the directory/filename:"), 'r')
			opsorderb = oldopsorder.read().replace('\n', '')
			opsorder = re.findall(r'[zerontwhfuiv]+', opsorderb)
		elif specifyops == "n":
			opsorder = ""
		elif specifyops == "N":
			opsorder = ""
		elif specifyops == "No":
			opsorder = ""
		elif specifyops == "no":
			opsorder = ""
		elif specifyops == "NO":
			opsorder = ""
		else:
			print "Please choose y/n:"


if opsorder == "":
	#if no opsorder has been found, or specified, create one.
	starthash = random.randint(50,100)
	starthashb = []
	for int in range(starthash):
		starthashb.append('five')
	endhash = random.randint(50,100)
	endhashb = []
	for int in range(endhash):
		endhashb.append('five')
	opsorder = random.sample(['zero', 'one', 'two', 'three', 'four', 'five', 'zero', 'one', 'two', 'three', 'four', 'five', 'zero', 'one', 'two', 'three', 'four', 'five', 'zero', 'one', 'two', 'three', 'four', 'five', 'zero', 'one', 'two', 'three', 'four', 'five', 'zero', 'one', 'two', 'three', 'four', 'five', 'zero', 'one', 'two', 'three', 'four', 'five', 'zero', 'one', 'two', 'three', 'four', 'five', 'zero', 'one', 'two', 'three', 'four', 'five', 'zero', 'one', 'two', 'three', 'four', 'five', ], 50)
	opsordertempa = starthashb+opsorder+endhashb
	opsorder = opsordertempa
	
	opsorders = map(str, [opsordertempa])
	opsorderz = ' '.join(opsorders)
	saveopsorder = open('opsorder.txt','w')
	saveopsorder.write(opsorderz)
	saveopsorder.close()
	print ""
	print "New Order of Operations Created, and saved as opsorder.txt"


###########Begin Hashing Operations##############

	
def zero():
	for str in password:
		a = base64.encodestring(password)
	return a

def one():
	for str in password:
		b = hashlib.sha512(password)
		c = b.hexdigest()
	return c
	
def two():
	for str in password:
		d = hashlib.md5(password)
		e = d.hexdigest()
	return e

def three():
		for str in password:
			i = hashlib.sha384(password)
			m = i.hexdigest()
		return m
def four():
		for str in password:
			i = hashlib.sha1(password)
			m = i.hexdigest()
		return m
def five():
		for str in password:
			i = hashlib.sha224(password)
			m = i.hexdigest()
		return m

	
d = { 'zero':zero, 'one':one, 'two':two, 'three':three, 'four':four, 'five':five }


#z = random.sample(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], 25)

#z = ['one', 'zero', 'two']

for cmd in opsorder:
	password = d[cmd]()
	print cmd
	print password
	print ""
raw_input('Press Enter to exit')
	
	
