from math import sqrt

def prime_sum(n):
	if n == 1:
		return 2

	counter = 1
	current = 3
	sum_primes = 2
	while counter < n:
		prime = True
		for i in range(2, int(sqrt(current)+1)):
			if current % i == 0:
				prime = False
		if prime:
			counter += 1
			sum_primes += current
		current += 1

	return sum_primes

"""
			for i in range(2, int(sqrt(n)+1)):
				if n % i == 0:
					prime = False
			if prime == True:
				print "yes"
			else:
				print "no"
"""
2, 3, 5, 7, 11

print "should be 2:", prime_sum(1)
print "should be 5:", prime_sum(2)
print "should be 10:", prime_sum(3)
print "should be 17:", prime_sum(4)
print "should be 28:", prime_sum(5)