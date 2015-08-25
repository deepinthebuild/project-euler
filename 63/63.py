UPPER_BOUND = 23 # Because magic


def DigitCount(input):
    return len(str(input))

count = 0

for digit in range(1, 10):
    for power in range(1, UPPER_BOUND):
        if DigitCount(digit ** power) == power:
            count += 1

print count
