import math 


UPPER_BOUND = 400000 # 9^5 times 6 is ~350,000, giving us a rough upper bound


def DigitFifthPowerSum(input):
    output = 0
    for digit in str(input):
        output += math.pow(int(digit),5)
    return output

total = 0

for x in range (2, UPPER_BOUND):
    if x == DigitFifthPowerSum(x):
        total += x

print total  
