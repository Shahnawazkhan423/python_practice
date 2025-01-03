class Codemos:
	def __init__(self,real,img):
		self.real=real
		self.img=img
	def show(self):
		if self.img<0:
			print("{}{}j".format(self.real,self.img))
		else:
			print("{}+{}j".format(self.real,self.img))
	def __add__(self,other):
		x = self.real+other.real 
		y = self.img+other.img
		return Codemos(x,y)

c1=Codemos(2,3)
c1.show()
c2 = Codemos(4,-4)
c2.show()
c3 = c1+c2
c3.show()