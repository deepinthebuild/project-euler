test_number = 600851475143
prime_list = []
d = 2

while (test_number > 1):
	while test_number % d == 0:
		prime_list.append(d)
		test_number /= d
	d += 1


print max(prime_list)
