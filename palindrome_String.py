user = input("Enter The palindrome Value: ")
backwards_Str = ""
for i in user:
	backwards_Str = i+backwards_Str
if user==backwards_Str:
	print("palindrome string",user)
else:
	print("Not palindrome string",user)

