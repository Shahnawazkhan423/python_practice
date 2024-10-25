name = input("Enter The Name:")
convert_n = ""
last_value = None
for i  in range (len(name)):
	if i==0:
		j = name[i].upper()
		convert_n+=j
		last_value = j

	else:
		if last_value==" ":
			j=name[i].upper()
			convert_n+=j
			last_value=j

		else:
			j=name[i].lower()
			convert_n+=j
			last_value=j
print(convert_n)
