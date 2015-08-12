GRID_DIMENSION = 20 #20x20
PRODUCT_LENGTH = 4
grid = []

#We only need to search in four directions due to symmetry: Down-Left, Down, Down-Right, Right

def RightProduct(input_array, row, column):
	product = 1
	if column + 4 >= GRID_DIMENSION:
		return 0
	else:
		for x in range(PRODUCT_LENGTH):
			product *= input_array[row][column + x] 
		return product

def DownProduct(input_array, row, column):
with open('grid.txt') as data:
	for line in data:
		grid.append(line.split())

print grid[19][20]
