import os
import sys
import time
import termcolor
import stdiomask

root = False
userCreated = False
userName = ""
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
	password = stdiomask(prompt = "")

def loading():
	for i in range(4):
		sys.stdout.write("")

validCommands = ["show", "whoami", "ping", "su root"]
cmd = input(f"{userName}@dannyOS:~{symbol()} ")