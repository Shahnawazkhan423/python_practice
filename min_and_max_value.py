List_1 = [-3,100,3,8,1.5,-100]
List_2 = []
List_3 = List_1
for i in range(len(List_1)):
	for j in range(i+1,len(List_1)):
		if List_1[i]>=List_1[j]:
			List_2.append(List_1[i])
			List_1.remove(List_1[i])
			print(List_2)

	
		