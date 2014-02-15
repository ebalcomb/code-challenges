from sys import stdin, stderr
from math import sqrt

def checkPrime():
	while 1:
	    try:
	        line = stdin.readline()
	        numbers = line.split()
	    except KeyboardInterrupt:
	        break

	    if not line:
	        break

	    for n in numbers:
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
				stderr.write("\'%s\' not an integer\n" %n)

checkPrime()
