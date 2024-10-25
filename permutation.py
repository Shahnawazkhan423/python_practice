n = int(input("Enter The N Value:"))
r = int(input("Enter The R Value:"))
fact_n = 1
for i in range(1,n+1):
	fact_n = fact_n*i
fact_r = 1
for j in range(1,n-r+1):
	fact_r = fact_r*j
perm = fact_n/fact_r
print(perm)