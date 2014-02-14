from sys import argv

input_file = open(argv[1])
number_sets = input_file.readlines()

def fizzbuzz(number_set):
	number_set = number_set.split()
	a = int(number_set[0])
	b = int(number_set[1])
	n = int(number_set[2])
	for i in range(1, n+1):
		if i % a == 0:
			if i % b == 0:
				print "FB",
			else:
				print "F",
		elif i % b == 0:
			print "B",
		else:
			print i,
	print


for number_set in number_sets:
	fizzbuzz(number_set)