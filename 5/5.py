#This is a trivial problem as stated. This code will find an arbitrary least common multiple.

upper_range = 20 
known_prime_list = []
output_list = []

def ListProduct(input_list):
	output = 1
	for k in input_list:
		output *= k
	return output

def IsPrime(input):
	for prime in known_prime_list:
		if input % prime == 0:
			return False
	return True

def PopulateFactorList(input, factor_list): #Very slow for big numbers
	d = input
	for factor in factor_list:
		if d % factor == 0:
			d /= factor
	if d != 1:
		factor_list.append(d)
		
					
#Populate our list of primes
for x in range(upper_range+1)[1:]:
	if x == 1:
		continue
	if not known_prime_list: #Empty lists are False
		known_prime_list.append(x)
		continue
	
	if IsPrime(x):
		known_prime_list.append(x)


output_list = known_prime_list

#Find our LCM which will probably include multiple primes
for x in range(upper_range+1)[2:]:
	PopulateFactorList(x, output_list)

#Debug help
#print output_list 	

print ListProduct(output_list)
