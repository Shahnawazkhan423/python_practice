def backwards_order(user):
	backwards_Str =""
	for i in user:#[::-1]
		backwards_Str = i+backwards_Str
	print(backwards_Str)

user = input("Enter The Value: ")
backwards_order(user)