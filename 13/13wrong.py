truncated_sum = 0
truncated_sum_digits = 10000000000

with open('numbers.txt') as number_list:
	for entry in number_list:
		truncated_sum += int(entry[:-10])
		truncated_sum = truncated_sum % truncated_sum_digits

print truncated_sum
