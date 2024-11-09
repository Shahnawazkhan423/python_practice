def color(room):
	height = float(input("Enter The Room Height:"))
	breath = float(input("Enter The Room Breadth:"))
	length = float(input("Enter The Room Lenght:"))
	cost = float(input("Enter The Cost of Color:"))
	litre = float(input("Enter The Litre of Color:"))
	calu = (length*breath)+(breath*height)*2+(length*height)*2
	divided_Cal = calu/litre
	quanity = divided_Cal*cost
	multiple_Quanity_Room = quanity*room
	return multiple_Quanity_Room

room = float(input("Enter The Room:"))
Room = color(room)
print("Total Cost:",Room)