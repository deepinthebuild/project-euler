

def LetterScore(character):
	return ord(character) - 64


def WordScore(word):
	character_list = list(word)
	score = 0
	for letter in character_list:
		score += LetterScore(letter)
	return score

with open('names.txt') as data:
	names = data.read().split(',')
	names = [entry.strip('\"') for entry in names]
	names = [entry.upper() for entry in names]
	names.sort()

total_score = 0

for position, name in enumerate(names):
	total_score += (WordScore(name) * (position + 1))

print total_score
