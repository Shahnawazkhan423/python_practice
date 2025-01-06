from Marke_Automation import*
class Inter_Mark:
	def Inter_Func(self):
	    choice = int(input("Press 1 for Creating Student Detail\nPress 2 Show All  Student Detail\nPress 3 Search  Student Detail\nPress 4 For Update  Student Detail\nPress 5 for Deleting  Student Detail\nPlease Enter Valid Choice: "))
	    if choice==1:
	    	inter = Inter_Function()
	    	inter.create_Deatil()
	    elif choice==2:
	    	inter = Inter_Function()
	    	inter.showall_Detail()
	    elif choice==3:
	    	inter = Inter_Function()
	    	inter.search_Detail()
	    elif choice==4:
	    	inter = Inter_Function()
	    	inter.update_Detail()
	    elif choice==5:
	    	inter = Inter_Function()
	    	inter.delete_Detail()
	    else:
	        print("Invalid Choice")
	        Inter_Func()
	    print("Welcome Student Detail")

Inter = Inter_Mark()
Inter.Inter_Func()    
temp = True
while temp==True:
    stu_Choice = input("Enter Y to Continue and N to Stop: ")
    if stu_Choice.lower()=="y":
        Inter.Inter_Func()
    else:
        print("Thanks Bye Bye")
        exit()
