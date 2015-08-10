#There's probably some slick solution to this with either more algebra than I care to do or linear programming.

# A < B < C
def SearchFunction():
	for C in range(1000):
		for B in range(C):
			for A in range(B):
				if ((A*A + B*B) == (C*C)) and (A + B + C == 1000):
					return (A*B*C)
			
print SearchFunction()
