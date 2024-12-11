class Rectangle:
	def __init__(self):
		self.length = int(input("Enter The Length Value: "))
		self.width  = int(input("Enter The Width  Value: "))
	def Calculate(self):
		return  self.length*self.width 
area = Rectangle()
Cal = area.Calculate()
print("Area Of Rectangle is :{},{}:{}".format(area.length,area.width,Cal))
