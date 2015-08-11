UPPER_BOUND = 1000000
biggest_chain_number = 1
biggest_chain_length = 1

def CollatzIterate(input):
	if input % 2 == 1:
		return input * 3 + 1
	else: 
		return input / 2

def CollatzChainLength(input):
	if input == 0:
		return 0
	chain_length = 0
	while input != 1:
		input = CollatzIterate(input)
		chain_length += 1
	return chain_length


for k in range(UPPER_BOUND):
	if CollatzChainLength(k) > biggest_chain_length:
		biggest_chain_number = k
		biggest_chain_length = CollatzChainLength(k)

print biggest_chain_number
	
