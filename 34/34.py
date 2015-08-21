import math


UPPER_BOUND = 3000000 	# 9 factorial times seven is only 2,540,160, giving us a rough upper bound.


def DigitFactorialSum(input):
	output = 0
	input_as_string = str(input)
	for digit in input_as_string:
		output += math.factorial(int(digit))
	return output

total = 0

for x in range(3, UPPER_BOUND):
	if x == DigitFactorialSum(x):
		total += x

print total		
