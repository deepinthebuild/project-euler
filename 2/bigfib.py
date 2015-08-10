import math
from time import time

a = 100

def Fibonacci(param):
	A = (1 + math.sqrt(5))/2
	B = (1 - math.sqrt(5))/2
	temp = (A**param - B**param) / math.sqrt(5)
	return int(round(temp))	

t = time()
	
a_fib = Fibonacci(a)

t = time() - t

print a_fib
print t	
