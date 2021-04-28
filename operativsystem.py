import os
import sys
import time
from termcolor import colored
import stdiomask

root = False
userCreated = False
rootPass = "root"

def symbol():
	if root == False:
		return "$"
	if root == True:
		return "#"

def createUser():
	wtf = " "
	name = input("Enter full name: ")
	userName = input("Enter preferred username: ")
	password = stdiomask.getpass(prompt = "Enter password: ", mask = "*")
	passwordConfirm = stdiomask.getpass(prompt = "Confirm password: ", mask = "*")
	if password == passwordConfirm:
		print(colored("Password created, proceeding to logiin", "green"))
	else:
		print(colored("Passwords doesn't match, try again", "red"))

def loading():
	for i in range(4):
		sys.stdout.write("")

def commands():
	if cmd == "whoami":
		if root == False:
			return userName 
		if root == True:
			return "root"

createUser()

validCommands = ["show", "whoami", "ping", "su root"]
cmd = input(f"{userName}@dannyOS:~{symbol()} ")
	