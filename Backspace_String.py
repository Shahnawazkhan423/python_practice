"""string_1  = "#bn#ew###e"
string_2  = "#bc#bs#"
Appened =[]
Appened_2 = []
for i in range(len(string_1)):
	if string_1[i]=='#':
		if len(Appened)!=0 and string_1[i+1]!=string_1[i]:
			Appened.pop()	
	else:
		Appened.append(string_1[i])
print("Added Item :",Appened)
for j in range(len(string_2)):
	if string_1[j]=='#':
		if j!=0:
			Appened_2.pop()
	else:
		Appened_2.append(string_2[j])
print(Appened_2)
if Appened == Appened_2:
	print("True")
else:
	print("False")
"""
def Backspace_Word(string):
    Appened =[]
    for i in range(len(string)):
	    if string[i]=='#':
		    if len(Appened)!=0:
			    Appened.pop()
	    else:
		    Appened.append(string[i])
    return Appened
    
string_First  = "#bc##bser#"
result = Backspace_Word(string_First)
print("First Strng :",result)
string_Sec = "#bc##bser#d"
result_Sec=  Backspace_Word(string_Sec)
print("Second String :",result_Sec)
if result==result_Sec:
    print(True)
else:
    print(False)
