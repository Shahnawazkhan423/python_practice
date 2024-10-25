'''name ="SHAHNAWAZKHAN"
print(name)
temp = name.lower()
print(temp)
temp1=temp.upper()
print(temp1)'''
#iterable Through Length of Variable
'''name = "ShahnawazKhan"
for i in range(len(name)):
	print(name[i])'''
#iterable through loop
'''name="ShahnawazKhan"
for i in name:
	print(i)
'''
#Concatienting	
'''first_Name = input("Enter First Name:")
last_Name = input("Enter Last Name:")
full_Name = first_Name+last_Name
for i in range
print(first_Name,last_Name,full_Name)'''
#Capatalize Frist Letter
'''name = "shahnawaz khan"
cap = name.capitalize()
print(cap)'''
#Casefold
name = "I love apples, apple are my favorite fruit"
text = name.casefold()
#Centre String
text = name.center(20,'O')
#count String Method
count = name.count("apple",10,21)#(value ,start,end)
#Check if the string ends with a punctuation sign (.):
end = name.endswith("t")
#The expandtabs() method sets the tab size to the specified number of whitespaces.
tabs = name.expandtabs(0)
#Where in the text is the word "welcome"?:
Find = name.find("apple")#(value, start, end)
#Decimal and Digit
decimal = "1234"
dec = decimal.isdecimal()
num =decimal.isdigit()
#Check if the string is a valid identifier
string = "khan 12"
Str = string.isidentifier()
#Join all items in a dictionary into a string, using the word "TEST" as separator:
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
Join = mySeparator.join(myDict)
#Return a 20 characters long, left justified version of the word "banana":
txt = "banana"
x = txt.ljust(20)
# Search for the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
txt = "i could eat bananas all day"
x = txt.partition("all day")
y = txt.split()
print(y)
