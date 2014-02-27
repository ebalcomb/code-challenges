from sys import stdin

def reverse_words(n):
	lines = n.readlines()
	for line in lines:
		words = line.split()
		if words:
			length = len(words)
			for i in range(length/2):
				temp = words[i]
				words[i] = words[length - i - 1]
				words[length - i - 1] = temp
			print " ".join(words)

reverse_words(stdin)