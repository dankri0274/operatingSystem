import os
import sys
import time
import stdiomask
from osLogin.py import *
from osCommands.py import *
from termcolor import colored

root = False
userCreated = False
rootPass = "root"
userName = ""

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
		print(colored("Password created, proceeding to login", "green"))
	else:
		print(colored("Passwords doesn't match, try again", "red"))

def loading():
	for i in range(4):
		sys.stdout.write("")

createUser()

validCommands = ["show", "whoami", "ping", "su root"]
cmd = input(f"{userName}@dannyOS:~{symbol()} ")
	