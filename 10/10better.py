SIEVE_HEIGHT = 2000000

def SieveSum(height):
	sieve = range(height+1)
	sieve[1] = 0
	sum = 0
	for x in range(height):
		if sieve[x]:
			sum += x
			for k in sieve[::x]:
				sieve[k] = 0
	return sum

print SieveSum(SIEVE_HEIGHT)
	
