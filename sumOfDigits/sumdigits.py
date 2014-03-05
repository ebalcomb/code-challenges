from sys import argv

def sum_of_digits(n):
	f = open(n).readlines()
	for line in f:
		summed = 0
		for char in str(line).strip():
			summed += int(char)
		print summed



sum_of_digits(argv[1])