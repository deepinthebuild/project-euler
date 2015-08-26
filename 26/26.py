
""" 
This algorithm does trial division until it reaches a step it has already done before, then returns the
cycle length.
"""

def UnitFractionCycleLength(denominator):
    division_list = []
    numerator = 10
    
    while (True):
        if numerator == 0:
            return 0

        numerator = numerator % denominator
        numerator *= 10

        if numerator in division_list:
            division_list += [numerator]
            break
        else:
            division_list += [numerator]

    for index, value in enumerate(division_list):
        if value == division_list[-1]:
            return (len(division_list) - index) - 1

max_denom = 0
max_cycle_length = 1

for x in range(2,1000):
    current_cycle_length = UnitFractionCycleLength(x)
    if current_cycle_length > max_cycle_length:
        max_cycle_length = current_cycle_length
        max_denom = x

print max_denom
