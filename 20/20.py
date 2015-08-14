# This is quite easy in Python as integers of arbitrary size are natively supported.

def Factorial(input):
	if input == 0:
		return 1
	product = reduce((lambda x, y: x * y), range(1, input+1))
	return product


factorialdigits = str(Factorial(100))
sum = 0
for digit in factorialdigits:
	sum += int(digit)

print sum
