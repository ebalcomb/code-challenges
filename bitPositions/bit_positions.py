from sys import stdin

def make_bin(n):
	return'{0:08b}'.format(int(n))


def bit_positions(n):
	lines = n.readlines()
	for line in lines:
		inputs = line.strip().split(",")
		whole = make_bin(inputs[0])
		a = -int(inputs[1])
		b = -int(inputs[2])
		if whole[a] == whole[b]:
			print "true"
		else: 
			print "false"

bit_positions(stdin)


# def bit_positions(n):
# 	lines = n.readlines()
# 	for line in lines:
# 		inputs = line.strip().split(",")
# 		whole = list(('{0:08b}'.format(int(inputs[0]))))
# 		length = len(whole)
# 		for i in range(length/2):
# 			temp = whole[i]
# 			whole[i] = whole[length-i-1]
# 			whole[length-i-1] = temp
# 		a = int(inputs[1])-1
# 		b = int(inputs[2])-1
# 		if whole[a] == whole[b]:
# 			print "true"
# 		else: 
# 			print "false"

# bit_positions(stdin)