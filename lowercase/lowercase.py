from sys import argv

def lowercase(n):
	f = open(n).readlines()
	for line in f:
		copy = ""
		for character in line:
			copy += character.lower()
		print copy,

lowercase(argv[1])