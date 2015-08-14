import math



def RemoveDuplicates(input_list):
	return list(set(input_list))


def DivisorList(input): # Only returns proper divisors, i.e. those strictly below input
	list_of_divisors = [1, ]
	for x in range(2, int(math.ceil(input ** 0.5)) + 1):
		if input % x == 0:
			list_of_divisors.append(x)
			list_of_divisors.append(input / x)
	return sorted(RemoveDuplicates(list_of_divisors))


def SumOfDivisors(input):
	return sum(DivisorList(input))


amicable_list = []
for x in range(1,10000):
	current_sum = SumOfDivisors(x)
	if x == SumOfDivisors(current_sum) and x != current_sum: # Exclude perfect numbers
		amicable_list.append(x) 

print sum(RemoveDuplicates(amicable_list))

