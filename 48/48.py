# Python's native integer operations are much much faster than my own version, so we'll use this.

sum = 0

for x in range(1,1001):
    sum += x ** x

print sum % 10000000000
