import math

total = 0
index = 0
current_fibonacci = 0
upper_limit = 4000000

def Fibonacci(param):
	A = (1 + math.sqrt(5))/2
	B = (1 - math.sqrt(5))/2
	temp = (A**param - B**param) / math.sqrt(5)
	return int(round(temp))	
	
while(current_fibonacci < upper_limit):
	if current_fibonacci % 2 == 0:
		total += current_fibonacci
	index += 1
	current_fibonacci = Fibonacci(index)

print total
	
