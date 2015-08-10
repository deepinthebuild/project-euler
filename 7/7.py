#wow such code reuse
#this is a very slow sieve

known_prime_list = []
desired_prime = 10001
index = 2

def IsPrime(input):
	for prime in known_prime_list:
		if input % prime == 0:
			return False
	return True


while len(known_prime_list) < desired_prime:
	
	if not known_prime_list: #Empty lists are False
		known_prime_list.append(index)
		index += 1
		continue
	
	if IsPrime(index):
		known_prime_list.append(index)
	index += 1


known_prime_list.sort()
print known_prime_list[-1]
