import math



UPPER_BOUND = 28123


def RemoveDuplicates(input_list):
	return list(set(input_list))


def DivisorList(input): # Only returns proper divisors, i.e. those strictly below input
	list_of_divisors = [1, ]
	if input == 2:
		return list_of_divisors
	for x in range(2, int(math.ceil(input ** 0.5)) + 1):
		if input % x == 0:
			list_of_divisors.append(x)
			list_of_divisors.append(input / x)
	return sorted(RemoveDuplicates(list_of_divisors))


def SumOfDivisors(input):
	return sum(DivisorList(input))


def IsAbundantNumber(input):
	if SumOfDivisors(input) > input:
		return True
	else:
		return False

def PairsList(input_list):
	index = 0
	pairs_list = []
	for first in input_list:
		for second in input_list[index:]:
			pairs_list.append((first, second))
		index += 1
	return pairs_list


abundant_list = []
abundant_list_pairs = []
abundant_sums = []
nonabundant_sums = []


for x in range(1,UPPER_BOUND):
	if IsAbundantNumber(x):
		abundant_list.append(x)

abundant_list_pairs = PairsList(abundant_list)

abundant_sums = map(sum, abundant_list_pairs)
abundant_sums = RemoveDuplicates(abundant_sums)
abundant_sums.sort()

while(abundant_sums[-1] >= UPPER_BOUND):
	abundant_sums.pop()

nonabundant_sums = list(range(1, UPPER_BOUND))

nonabundant_sums = list(set(nonabundant_sums) - set(abundant_sums))
nonabundant_sums.sort()

print sum(nonabundant_sums)
