temp=0
user = 98
Length = 0
for i in range(1,user+1):
	if i%7!=0:
		temp+=i
		Length+=1

Average=temp/Length
print("Total Length ",Length)
print("Total Sum",temp)
print("Total Average",Average)