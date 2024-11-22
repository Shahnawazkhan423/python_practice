#Create Dict
dict1 = {"Name":"Amber","Age":18,"Contact":8546293965,"Weight":84.5}
"""print(dict1)
print(type(dict1))"""
#***************************
#Read Dict
#Key Access
"""for i in dict1:
	print("Keys :",i)
print()
#Value Access
for j in dict1.values():
	print("Values :",j)
print()

for i in dict1:
	print(dict1[i])
print()	
#Key and Value Both Access
for k,n in dict1.items():
	print("Key :{} And Values :{}".format(k,n))
"""
#*********************************************
#Adding Value Key Value Pair
#Adding Value
dict_Add = dict1["Email"]="xyz@gmail.com"
print(dict_Add)
print(dict1)
print()
dict_Update = dict1["Name"]="Ankit"
print(dict_Update)
print(dict1)
print()
dict_Remove = dict1.remove("Name")
print(dict_Remove)
print(dict1)
print()