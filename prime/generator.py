import sys
from random import getrandbits

def number_generator():
	while True:
		n = getrandbits(16)
		sys.stdout.write(str(n) + "\n")

number_generator()

