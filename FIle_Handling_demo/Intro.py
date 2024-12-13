name = "Shahnawaz Khan"
Address ="167k Sector Green Park Indore"
Mob = "7067606682"
f1 =  open("Sample.txt","w")
entry = "{}\n{}\n{}".format(name,Address,Mob)
f1.write(entry)
f1.close()
f2 = open("Sample.txt","r")
x = f2.read()
print(x)
f2.close() 

