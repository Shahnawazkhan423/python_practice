user = float(input("Enter The Grade Number:-"))
integerValue = int(user)
if integerValue!=user:
	print("Invaid syntex")
elif integerValue<=100 and integerValue>=90:
	print("O grade")
elif integerValue<=89 and integerValue>=80:
 	print("A Grade")
elif integerValue<=79 and integerValue>=70:
 	print("B Grade")
elif integerValue<=69 and integerValue>=60:
 	print("C Grade")
else:
 	print("Fail")
