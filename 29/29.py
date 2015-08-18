import math


UPPER_BOUND = 101


def RemoveDuplicates(input_list):
	return list(set(input_list))


distinct_powers = []

for a in range(2,UPPER_BOUND):
	for b in range(2, UPPER_BOUND):
		distinct_powers.append(math.pow(a, b))

distinct_powers = RemoveDuplicates(distinct_powers)

print len(distinct_powers)
