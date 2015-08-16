import itertools


INDEX = 1000000


permutation_list = list(itertools.permutations(range(10)))
permutation_list.sort()

output = list(permutation_list[INDEX - 1])
output = map(str, output)

print ''.join(output)

