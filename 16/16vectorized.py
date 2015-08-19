import itertools


class VectorizedNumber(object):

	def __init__(self, input_number):
		self.digits = []
		
		if isinstance(input_number, (int, long)):
			self.digits = [int(digit) for digit in str(input_number)[::-1]]
		else:
			self.digits = input_number
			
		self.length = len(list(self.digits))


	def rectify(self):
		self.digits.append(0)
		for index in range(len(self.digits) - 1):
			while(self.digits[index] >= 10):
				self.digits[index] -= 10
				self.digits[index+1] += 1
		
		while(self.digits[-1] == 0):
			del self.digits[-1]
		
		self.length = len(list(self.digits))			

	
	def digital_sum(self):
		return sum(self.digits)				


	def __add__(self, other):

		output = VectorizedNumber(0)
		output.digits = [sum(x) for x in itertools.izip_longest(list(self.digits), 
										list(other.digits), 
										fillvalue=0)]
		output.rectify()
		return output


	def __mul__(self, other):
		output_length = self.length + other.length - 1
		output = VectorizedNumber([0] * output_length)
		for self_index, self_value in enumerate(self.digits):
			for other_index, other_value in enumerate(other.digits):
				output.digits[self_index+other_index] += self_value * other_value
		output.rectify()
		return output


	def __pow__(self, exponent):
		if exponent == 0:
			return VectorizedNumber(1)
		elif exponent == 1:
			return self
		elif exponent % 2 == 0:
			return (self * self)**(exponent/2)
		else:
			return self * (self * self)**((exponent-1)/2)

		
	def __str__(self):
		return ''.join(str(x) for x in self.digits[::-1])



kay = VectorizedNumber(2) ** 1000

print kay.digital_sum()
