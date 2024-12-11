List1 =[10,30,60,50]
for i in range(0,len(List1)):
     for j in range(i+1,len(List1)):
      	 if List1[i]>=List1[j]:
            List1[i],List1[j]=List1[j],List1[i]
            print(List1)