GRID_DIMENSION = 20 #20x20
PRODUCT_LENGTH = 4

#We only need to search in four directions due to symmetry: Down-Left, Down, Down-Right, Right

def RightProduct(input_array, row, column):
	product = 1
	if column + PRODUCT_LENGTH >= GRID_DIMENSION:
		return 0
	else:
		for x in range(PRODUCT_LENGTH):
			product *= input_array[row][column + x] 
		return product

def DownProduct(input_array, row, column):
	product = 1
	if row + PRODUCT_LENGTH >= GRID_DIMENSION:
		return 0
	else:
		for x in range(PRODUCT_LENGTH):
			product *= input_array[row + x][column]
		return product

def DownRightProduct(input_array, row, column):
	product = 1
	if row + PRODUCT_LENGTH >= GRID_DIMENSION:
		return 0
	elif column + PRODUCT_LENGTH >= GRID_DIMENSION:
		return 0
	else:
		for x in range(PRODUCT_LENGTH):
			product *= input_array[row + x][column + x]
		return product

def DownLeftProduct(input_array, row, column)

with open('data.txt') as data:
	grid = []
	for line in data:
		grid.append(line.split())
	print map(max, grid) 
