biggest_palindrome = 0
ceiling = 1000

def IsPalindrome(input):
	temp_input = str(input)
	return temp_input == temp_input[::-1]

for x in range(ceiling):
	for y in range(ceiling):
		if IsPalindrome(x*y) and biggest_palindrome < (x*y):
			biggest_palindrome = (x*y)

print biggest_palindrome
