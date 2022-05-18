# Imports the regular expression library
import re as re

# Opens txt file
f = open("phonebook.txt", "r")
f = f.read()
f = f.split()

for i in f:
	if re.["a"-"z"] or re.[0-9] or re.["A"-"Z"] not in i:
