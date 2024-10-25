start = int(input("Enter The Number:"))
end = int(input("Enter The End Value:"))
convert = ""
if start>1:
	for i in range(start,end):
		for j in range(2,i):
			if i%j==0:
				break
		else:
			Cont = "{},".format(i)
			convert+=Cont
	print("Prime Number",convert)	
else:
	print("Negative Number Not Allowed")
