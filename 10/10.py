#Slow sieve to find all primes below two million and then their sum.

SIEVE_HEIGHT = 2000000
		
known_prime_list = []
def IsPrime(input):
	for prime in known_prime_list:
		if input % prime == 0:
			return False
	return True

for x in range(SIEVE_HEIGHT+1)[1:]:
	if x == 1:
		continue
	if not known_prime_list: #Empty lists are False
		known_prime_list.append(x)
		continue
	
	if IsPrime(x):
		known_prime_list.append(x)

print sum(known_prime_list)
