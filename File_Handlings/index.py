from phone_Book_funtion import*
from Import_Cont import*
from Export_Contact import*
def phone_Book():
    choice = int(input("Press 1 for Creating Contact\nPress 2 Show All Contact\nPress 3 Search Contact\nPress 4 For Update Contact\nPress 5 for Deleting\nPress 6 for Import\nPress 7 for Export\nPlease Enter Valid Choice: "))
    if choice==1:
        create_contact()
    elif choice==2:
        showall_contact()
    elif choice==3:
        search_contact()
    elif choice==4:
        update_contact()
    elif choice==5:
        delete_contact()
    elif choice==6:
        import_cvs()
    elif choice==7:
        export()
    else:
        print("Invalid Choice")
        phone_Book()
    print("Welcome My Phone Book")
phone_Book()       
temp = True
while temp==True:
    cont_Choice = input("Enter Y to Continue and N to Stop: ")
    if cont_Choice.lower()=="y":
        phone_Book()
    else:
        print("Thanks Bye Bye")
        exit()

