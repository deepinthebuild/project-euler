class NumbersList:
    
    def __init__(self):
        self.contents = []

    def TrianglePopulate(self, upper_range):
        for x in range(1, upper_range+1):
           self.contents.append(NthTriangularNumber(x))

    def Contains(self, query):
        if query in self.contents:
            return True
        else: 
            return False


def NthTriangularNumber(input):
    return input * (input + 1) / 2


def LetterScore(character):
    return ord(character.upper()) - 64


def WordScore(word):
    score = 0
    for letter in word:
        score += LetterScore(letter)
    return score


Triangle_Word_Count = 0

with open('words.txt') as data:
    names = data.read().split(',')

names = [entry.strip('\"') for entry in names]
name_scores = [WordScore(name) for name in names]

TriangleNumberList = NumbersList()
TriangleNumberList.TrianglePopulate(30)

for score in name_scores:
    if TriangleNumberList.Contains(score):
        Triangle_Word_Count +=1

print Triangle_Word_Count
