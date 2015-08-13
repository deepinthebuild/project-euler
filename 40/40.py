count = 0
champernowne = ''
product = 1

while(len(champernowne) < 1000001):
	champernowne = champernowne + str(count)
	count += 1

for n in range(7):
	product *= int(champernowne[10**n])

print product
	
