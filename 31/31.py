# This finds the solution using truncated generating functions.

GOAL = 200
coin_denominations = [2, 5, 10, 20, 50, 100, 200]


class CoinCombinations:
   
    def __init__(self, denomination):
        if denomination == 0:
            self.combination_vector = [1] + [0] * GOAL
        else:
            self.combination_vector = [1]
            denomination_vector = [0] * (denomination - 1) + [1] # input = 5 means we get [0 0 0 0 0 1]
            self.combination_vector += denomination_vector * ((GOAL / denomination) + 1)

    
    def product(self, other):
        output = CoinCombinations(0)
        for self_index, self_value in enumerate(self.combination_vector):
            for other_index, other_value in enumerate(other.combination_vector):
                if 0 < (self_index + other_index) <= GOAL:
                    output.combination_vector[self_index+other_index] += self_value * other_value
        return output


CoinVector = CoinCombinations(1)

for entry in coin_denominations:
    CoinVector = CoinVector.product(CoinCombinations(entry))

print CoinVector.combination_vector[200]
