"""user = input("Enter The palindrome Value: ")
backwards_Str = ""
for i in user:
    backwards_Str = i+backwards_Str
if user==backwards_Str:
    print("palindrome string",user)
else:
    print("Not palindrome string",user)"""
#************************************
num= 121
temp = num  
revrev = 0  
while num!=0 and num>0:  
    dig = num % 10 
    revrev = revrev  * 10 + dig   
    numnum = num // 10  
if(temp == revrev ):  
    print("This value is a palindrome number!")  
else:  
    print("This value is not a palindrome number!")  
