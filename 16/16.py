bigstring = str(2**1000) #Luckily we can represent this exactly
sum = 0

for x in range(len(bigstring)):
	sum += int(bigstring[x])

print sum
