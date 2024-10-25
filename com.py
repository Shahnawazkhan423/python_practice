n = int(input("Enter The N Value:"))
r = int(input("Enter The R Value:"))
if n>r:
	fact_n = 1
	for i in range(1,n+1):
		fact_n = fact_n*i
	fact =1
	for k in range(1,r+1):
		fact = fact*k
	fact_r = 1
	for j in range(1,n-r+1):
		fact_r = fact_r*j
	com = fact_n/(fact_r*fact)
	print(com)
else:
	print("Invalid Syntax")