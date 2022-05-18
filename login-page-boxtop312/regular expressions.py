# Imports the regular expression library
import re as re

# Opens txt file
f = open("phonebook.txt", "r")
f = f.read()
f = f.split()
z = open("chips.txt", "r")
z = z.read()
z = z.split()


def firstthing(f):
	for i in f:
		if re.search("[a-z]", i):
			pass
		else:
			return False

def secthing(z):
	for i in z:
		if re.search("[a0]", i) or re.search("[ab]", i)

print(firstthing("a"))
