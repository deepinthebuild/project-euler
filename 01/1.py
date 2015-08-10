index = 0
total = 0

while (index < 1000):
	if (index % 3 == 0) or (index % 5 == 0):
		total += index
	index += 1
print index
print total
