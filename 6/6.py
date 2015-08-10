def SquareOfSums(input): #sums from 1 to input
	output = 0
	for x in range(input):
		output += (x+1)
	return output*output

def SumOfSquares(input):
	output = 0
	for x in range(input):
		output += ((x+1)*(x+1))
	return output
	
print SquareOfSums(100) - SumOfSquares(100)
