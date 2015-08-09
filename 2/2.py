total = 0
index = 0
current_fibonacci = 0
upper_limit = 4000000

def Fibonacci(param):
	if param == 1:
		return 1
	if param == 2:
		return 2
	return Fibonacci(param-1) + Fibonacci(param-2)
		
while(current_fibonacci < upper_limit):
	if current_fibonacci % 2 == 0:
		total += current_fibonacci
	index += 1
	current_fibonacci = Fibonacci(index)

print total
	
