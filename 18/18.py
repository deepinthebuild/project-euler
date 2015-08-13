triangle = []

def PairwiseMaximum(input_list):
	output_list = []
	for x in range(len(input_list) - 1):
		output_list.append(max(input_list[x], input_list[x + 1]))
	return output_list

#Crunches the bottom row in the row above it
def TriangleCollapse(list_of_lists):
	working_entry = list_of_lists
	bottom = working_entry.pop()
	second_to_bottom = working_entry.pop()
	new_entry = [sum(x) for x in zip(second_to_bottom, PairwiseMaximum(bottom))]
	working_entry.append(new_entry)
	return working_entry

with open('data.txt') as data:
	for line in data:
		triangle.append(line.split())
	triangle = [[int(k) for k in line] for line in triangle]

while(len(triangle) != 1):
	triangle = TriangleCollapse(triangle)

print triangle
