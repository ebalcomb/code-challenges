from sys import argv
from math import sqrt


def checkPrime(n):
	try:
		n = int(n)
		if n > 1:
			for i in range(2, int(sqrt(n)+1)):
				if n % i == 0:
					return False
			return True
		else:
			return False
	except ValueError:
		return "warning: \'%s\' is not an integer" %n



print checkPrime(argv[1])




