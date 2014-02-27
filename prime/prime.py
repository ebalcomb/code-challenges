from sys import argv
from math import sqrt


def check_prime(n):
	prime = True
	try:
		n = int(n)
		if n > 1:
			for i in range(2, int(sqrt(n)+1)):
				if n % i == 0:
					prime = False
			if prime == True:
				print "yes"
			else:
				print "no"
		else:
			print "no"
	except ValueError:
		print "warning: \'%s\' is not an integer" %n


checkPrime(argv[1])




