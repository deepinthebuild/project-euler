def TriangularNumber(N): #returns the Nth triangular number
	if N == 0:
		return 0
	return (N * (N + 1)) / 2

def NumberOfDivisors(input_number): #returns the number of divisors for the given input
	number_of_divisors = 2 #Any number is divisible by 1 and itself
	div = 2
	while(div**2 <= input_number): #Check only up to sqrt(N)
		if input_number % div == 0:
			number_of_divisors += 2 #divisors come in pairs
		div += 1
	return number_of_divisors

index=1
while(NumberOfDivisors(TriangularNumber(index)) <= 500):
	index += 1

print "Your number is " + str(TriangularNumber(index))
print "The number of divisors is " + str(NumberOfDivisors(TriangularNumber(index)))
