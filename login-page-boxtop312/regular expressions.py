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
	newlist = []
	return re.search("^a(b*)$", z)
	# 	newlist.append(z)
	# else:
	# 	pass
	# return newlist

print(secthing(f))
