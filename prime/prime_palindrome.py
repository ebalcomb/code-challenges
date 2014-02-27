from math import sqrt

def prime_palindrome(n):
	for j in range(n, 0, -1):
		if len(str(j)) > 1 and str(j) == str(j)[::-1]:
			prime = True
			for i in range(2, int(sqrt(j)+1)):
				if j % i == 0:
					prime = False
			if prime:
				return j
	return "no prime palindromes smaller than %s" %n

print prime_palindrome(1000)
