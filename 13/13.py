good_enough_sum = 0

with open('numbers.txt') as number_list:
	for entry in number_list:
		good_enough_sum += int(entry[:15])

print str(good_enough_sum)[:10]
