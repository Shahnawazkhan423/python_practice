def fab(end):
	first_num = 0
	sec_num = 1
	count = 0
	while count<=end:
		print(count)
		first_num = sec_num
		sec_num = count
		count = first_num+sec_num
end = int(input("Enter The End Number:"))
fab(end)