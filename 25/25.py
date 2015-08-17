import numpy as np


def Fibonacci(input):
	fib_vector = np.array( [[1], [1]], dtype='object' )
	M = np.array( [[1,1], [1,0]], dtype='object')
	M = np.linalg.matrix_power(M, input - 1)
	output = np.dot(M, fib_vector)
	return output.item(1)



index = 1
length = 1

while(length < 1000):
	index += 1
	length = len(str(Fibonacci(index)))

print index
