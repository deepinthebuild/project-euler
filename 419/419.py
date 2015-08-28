"""
 Data file on the look and say sequence copied from
 http://www.njohnston.ca/2010/10/a-derivation-of-conways-degree-71-look-and-say-polynomial/
"""


import itertools
import numpy as np



START_DEPTH = 10
DEPTH = 40
MODULUS = 2**30
LOOKANDSAY_TEN = [45, 71]

lookandsaydata = []

transitionlookup = {}




def UnParenthesize(entry):
    output = ''
    for character in entry:
        if character == '(' or character == ')':
            output += ' '
        else: 
            output += character
    output = output.split()
    output = [int(x) for x in output]   
    return output


def NumberOfCharactersInString(input_string, character):
    count = 0
    for entry in input_string:
        if entry == character:
            count += 1
    return count

def ConwayArray(element):
    output = [0] * 92
    for descendant in transitionlookup[element]:
        output[descendant-1] = 1
    return output

def ConwayTest(list):
    for x in range(len(list)):
        if list[x]:
            print x+1,
    print ''
#############################################

binary_string = bin(DEPTH - START_DEPTH)[2:]
binary_string = binary_string[::-1]



with open('data.txt') as datafile:
    for line in datafile:
        lookandsaydata.append(line.split())

for x in range(len(lookandsaydata)):
    transitionlookup[x+1] = UnParenthesize(lookandsaydata[x][3])


OnesWeightVector = np.array([NumberOfCharactersInString(lookandsaydata[x][1], '1') for x in range(92)], dtype=object)
TwosWeightVector = np.array([NumberOfCharactersInString(lookandsaydata[x][1], '2') for x in range(92)], dtype=object)
ThreesWeightVector = np.array([NumberOfCharactersInString(lookandsaydata[x][1], '3') for x in range(92)], dtype=object)


ConwayStack = [ConwayArray(x) for x in range(1,93)]

ConwayStartMatrix = np.matrix(ConwayStack, dtype=object)
#ConwayMatrix_2 = np.linalg.matrix_power(ConwayStartMatrix, 2)
ConwayMatrix = np.identity(92, dtype=object)

"""
for x in range(20):
    ConwayMatrix = np.dot(ConwayMatrix, ConwayStartMatrix)
"""
ConwayMatrix = np.linalg.matrix_power(ConwayStartMatrix, DEPTH - START_DEPTH)

"""
for index, key in enumerate(binary_string):
    if index == 0:
        continue
    elif key == '1':
        ConwayMatrix = np.dot(ConwayMatrix, np.linalg.matrix_power(ConwayMatrix_2,index+1))
"""
print int(np.dot(ConwayMatrix[44], OnesWeightVector) + np.dot(ConwayMatrix[70], OnesWeightVector)) % MODULUS,
print int(np.dot(ConwayMatrix[44], TwosWeightVector) + np.dot(ConwayMatrix[70], TwosWeightVector)) % MODULUS,
print int(np.dot(ConwayMatrix[44], ThreesWeightVector) + np.dot(ConwayMatrix[70], ThreesWeightVector)) % MODULUS,
