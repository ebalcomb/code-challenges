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
		return "Please input an integer"


# print "A: ", checkPrime("A")
# print "1.5: ", checkPrime(1.5)
# print "-5: ", checkPrime(-5)
# print "0: ", checkPrime(0)
# print "1: ", checkPrime(1)
# print "2: ", checkPrime(2)
# print "3: ", checkPrime(3)
# print "4: ", checkPrime(4)
# print "5: ", checkPrime(5)
# print "6: ", checkPrime(6)
# print "7: ", checkPrime(7)
# print "8: ", checkPrime(8)


print checkPrime(argv[1])




