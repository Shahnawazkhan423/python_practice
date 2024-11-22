a = 5
b = 8 
#Without Temp Varible
a = a+b
b = a-b
a = a-b
print(a,b)
#With Temp Variable
temp = a 
a = b
b = temp		
print(a,b)
