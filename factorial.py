num = int(input("Enter The Factorial Number: "))
if num < 0:
	print("Negative Input Factorial is not defined")
else :
	fact=1
	for i in range(num+1,1,-1):
		fact*=i
#print("Factorial of",num,"=",fact)
#print("Factorial of "+str(num)+" = "+str(fact)) 
print("Factorial of {} = {}".format(num,fact))