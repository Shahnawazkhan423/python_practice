class square:
	def __init__(self):
		self.side = int(input("Enter Side:"))
	def area(self):
		return self.side*self.side
	def perimeter(self):
		return 4*self.side
s1 = square()
p1 = s1.perimeter()
a1 = s1.area()
print("Area Of Square with side {} = {} ".format(s1.side,a1))