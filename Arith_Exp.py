#*******Expression******
#3+12-23/8*2
#23-23+3/33/33-12*12
#5 + 3 * 2 - 8 / 4
#10 - 4 + 2 * 3
#15 / 3 + 2 - 7 * 2
#***********Infix TO Postifx***********
#correct_convert = ["3","12","+","23","8","/","2","*","-"]
#correct_convert = ["23","23","-","3","33","/","33","/","+","12","12","*","-"]
#correct_convert = ["5","3","2","*","+","8","4","/","-"]
#correct_convert = ["10","4","-","2","3","*","+"]
correct_convert = ["15","3","/","2","+","7","2","*","-"]
#***************Infix TO Prefix******
#correct_convert_Prefix = ["+","3","-","12","*","/","23","8","2"]
#correct_convert_Prefix = ["-","23","+","23","-","/","3","/","33","33","*","12","12"]
#correct_convert_Prefix = ["-","+","5","*","3","2","/","8","4"]
correct_convert_Prefix = ["-","+","/","15","3","2","*","7",""]


class stack:
    """docstring for stack"""
    def __init__(self):
        self.stacklist  = []
        self.max = -1 

    def show(self) : 
        print("Stacklist : ", self.stacklist)

    def push(self,x):
        self.stacklist.append(x)
        self.max = self.max + 1 

    def pop(self) : 
        z = self.stacklist.pop()
        self.max = self.max-1
        return z 
        
def validate_exp(x):
    operator_index = []
    for i in range(len(x)):
        if x[i] in operator : 
            operator_index.append(i)

    print("Operator Indics : ", operator_index)

    for j in operator_index : 
        if j == 0 or j % 2 == 0 or j == len(x)-1:
            return False
    else : 
        return True 


A= input("Enter Experssion : ")
operator={"/":2,"*":2,"-":1,"+":1}
exp=[]
term=""
for i in A:
    if i not in operator:
        term = term+i
    else:
        if term!="":
            exp.append(term)
        exp.append(i)
        term=""
else:
    if term!="":
        exp.append(term)
print("Expression :",exp)

y = validate_exp(exp)
if y == True : 
    print("Valid Exp")
    #convert Infix to Postfix 
    post_exp = []
    Temp = stack()
    for i in exp : 
        if i not in operator : 
            post_exp.append(i)
        else : 
            if Temp.max == -1 :
                Temp.push(i)
            else : 
                while  Temp.max !=-1  and operator[Temp.stacklist[Temp.max]] >= operator[i] : 
                    m = Temp.pop()
                    post_exp.append(m)
                Temp.push(i)
    else : 
        while Temp.max !=-1 :
            m = Temp.pop()
            post_exp.append(m)

    #convert Infix to Prefix 
    prefix_exp = []
    Temp_pref = stack()
    for i in exp[::-1] : 
        if i not in operator : 
            prefix_exp.append(i)
        else : 
            if Temp_pref.max == -1 :
                Temp_pref.push(i)
            else : 
                while  Temp_pref.max !=-1  and operator[Temp_pref.stacklist[Temp_pref.max]] >= operator[i] : 
                    m = Temp_pref.pop()
                    prefix_exp.append(m)
                Temp_pref.push(i)
    else : 
        while Temp_pref.max !=-1 :
            m = Temp_pref.pop()
            prefix_exp.append(m)





    Temp.show()
    print("Generated Postfix : ",post_exp)
    print("Correct Postfix : ",correct_convert)
    Temp_pref.show()
    print("Generated Prefix : ",prefix_exp[::-1])
    print("Correct Prefix : ",correct_convert_Prefix)




else : 
    print("Invalid Exp ")

def evaluation_postfix(evaluat):
    result = stack()
    for i in post_exp:
        if i not in operator:
            result.push(int(i))
        else:
            y = result.pop()
            x = result.pop()
            if i=="+":
                result.push(x+y)
            elif i=="-":
                result.push(x-y)    
            elif i=="*":
                result.push(x*y)   
            elif i=="/":
                result.push(x/y)

    return result.pop()

Postfix = evaluation_postfix(post_exp)
print("Final Result Postfix is:",Postfix)

Prefix = evaluation_postfix(prefix_exp)
print("Final Result Prefix is :",Prefix)