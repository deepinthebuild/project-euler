#The problem asks for non-whitespace characters only so we won't worry about spacing.

UPPER_RANGE = 1000

words_for_numbers = 	{1:'one',
			2:'two',
			3:'three',
			4:'four',
			5:'five',
			6:'six',
			7:'seven',
			8:'eight',
			9:'nine',
			10:'ten',
			11:'eleven',
			12:'twelve',
			13:'thirteen',
			14:'fourteen',
			15:'fifteen',
			16:'sixteen',
			17:'seventeen',
			18:'eighteen',
			19:'nineteen',
			20:'twenty',
			30:'thirty',
			40:'forty',
			50:'fifty',
			60:'sixty',
			70:'seventy',
			80:'eighty',
			90:'ninety',
			0:''}


#Lots of special cases here
def IntToText(input):
	input_digits = list(str(input))
	input_digits = [int(j) for j in input_digits]
	
	if input == 1000:
		return 'onethousand'	
	if input < 20:
		return words_for_numbers[input]
	if input < 100:
		return words_for_numbers[input_digits[0] * 10] + words_for_numbers[input_digits[1]]
	if input % 100 == 0:
		return words_for_numbers[input_digits[0]] + 'hundred'
	if input % 100 < 20:
		return words_for_numbers[input_digits[0]] + 'hundred' + 'and' + words_for_numbers[input % 100]
        return words_for_numbers[input_digits[0]] + 'hundred' + 'and' + words_for_numbers[input_digits[1] * 10] + words_for_numbers[input_digits[2]]

total = 0

for x in range(1,1001):
	total += len(IntToText(x))

print total
