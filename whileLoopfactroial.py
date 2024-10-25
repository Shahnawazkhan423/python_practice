num = int(input("Enter Factorial Number:"))
if num<0:
	print("Negative Input Factorial is not defined{}".formate(num))
else:
	fact=1
	i=1
	while (i<=num):
		fact*=i
		i+=1
	print("Factorial of {} = {}".format(num,fact))
