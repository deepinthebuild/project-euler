UPPER_BOUND = 1000000


def IsPalindrome(input):
    input_str = str(input)
    if input_str == input_str[::-1]:
        return True
    else:
        return False


def BinaryString(input):
    output = bin(input)[2:]
    return output


def IsPalindromeInBothBases(input):
    if IsPalindrome(input) and IsPalindrome(BinaryString(input)):
        return True
    else: 
        return False


output = 0

for x in range(UPPER_BOUND):
    if IsPalindromeInBothBases(x):
        output += x

print output
