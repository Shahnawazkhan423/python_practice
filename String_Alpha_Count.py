user = "abbfda"
string =""
count=1
for i in range(1,len(user)):
    if user[i]==user[i-1]:
        count+=1
    else:   
        string+=(user[i-1]+str(count))
        count=1
string+=(user[i]+str(count))
print(string)
