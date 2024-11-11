"""user = int(input("How Many Type Enter Value:"))
List1 =[]
Temp =0
List2=[]
for i  in range(1,user+1):
	Value=int(input("Enter The Value:"))
	List1.append(Value)
print(List1)
for j in range(len(List1)):
	Temp+=List1[j]
	List2=Temp
print("Total Sum: ",List2)

print("Average: ",List2/user)"""
#*********************************
def List_Average_Find(user):
	Temp =0
	List1 =[]
	List2=[]
	for i  in range(1,user+1):
		Value=int(input("Enter The Value:"))
		List1.append(Value)
	print(List1)
	for j in range(len(List1)):
		Temp+=List1[j]
		List2=Temp
	return List2

user = int(input("How Many Type Enter Value:"))
result = List_Average_Find(user)
print("Total Sum is: ",result)
print("Average is:",result/user)