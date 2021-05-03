from os import *
import stdiomask

usedAll = False
maxTries = 5
tries = 0


class accLogin:
	def login():
		usrLogin = input("Username: ")
		pswdLogin = stdiomask.getpass(prompt = "Password: ", mask = "*")
		if userName == usrLogin and password == pswdLogin:
			print(colored(f"\n{name} logged in as: {userName}\n", "green"))
		else:
			print(colored("\nUsername or password incorrect\n", "red"))
