GRID_DIMENSION = 20 #20x20
PRODUCT_LENGTH = 4

#We only need to search in four directions due to symmetry: Down-Left, Down, Down-Right, and Right


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


def DownLeftProduct(input_array, row, column):
	product = 1
	if column < 3:
		return 0
	elif row + PRODUCT_LENGTH >= GRID_DIMENSION:
		return 0
	else:
		for x in range(PRODUCT_LENGTH):
			product *= input_array[row + x][column - x]
		return product

def MaxDirectionalProduct(input_array, row, column):
	MaxProduct = 0
	MaxProduct = max(RightProduct(input_array, row, column), MaxProduct)
	MaxProduct = max(DownProduct(input_array, row, column), MaxProduct)
	MaxProduct = max(DownRightProduct(input_array, row, column), MaxProduct)
	MaxProduct = max(DownLeftProduct(input_array, row, column), MaxProduct)
	return MaxProduct


with open('data.txt') as data:

#Get our data in to a nice array

	grid = []
	for line in data:
		grid.append(line.split())

#Make sure all of the data is of the right type
	for row in range(GRID_DIMENSION):
		for column in range(GRID_DIMENSION):
			grid[row][column] = int(grid[row][column])
	
#Run each product over each entry in the array. The functions themselves take care of the array boundaries.		

	LargestProduct = 0
	for row in range(GRID_DIMENSION):
		for column in range(GRID_DIMENSION):
			LargestProduct = max(LargestProduct, MaxDirectionalProduct(grid, row, column))

	print LargestProduct	
