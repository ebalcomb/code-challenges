from math import sqrt

def prime_sum(n):
	if n == 1:
		return 2

	counter = 1
	current = 2
	sum_primes = 2
	while counter <= n:
		prime = True
		for i in range(2, int(sqrt(current)+1)):
			if current % i == 0:
				prime = False
		if prime:
			counter += 1
			sum_primes += current
		current += 1

	return sum_primes



print prime_sum(1)
print prime_sum(2)
print prime_sum(3)
print prime_sum(4)
print prime_sum(5)