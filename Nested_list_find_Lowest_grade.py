python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
Sorted_New_List1= []

for Sort in range(len(python_students)):
	Sorted_List = sorted(python_students,key=lambda x:x[1])
	if Sort==1:
		Sorted_New_List1.append(Sorted_List[Sort])
print(Sorted_New_List1)
	
