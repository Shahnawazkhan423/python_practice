def circle(i):
	if i%3==0:
		area = 3.14*i*i	
		circum = 2*3.14*i
		print("Area of Circle Radius is {} over {}".format(i,area))
		print("Circumferece of Circle  Radius is {} over {}".format(i,circum))
		print()

for i in range (10,31):
	circle(i)
