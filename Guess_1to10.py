i=1
while i>0:
	guess = int(input('Guess The Number  between 1 and 10:'))
	if guess>0:
		if guess==7:
			print("Congratulations! You guessed it right.")
			break
		elif guess>10:
			print("Invalid Syntax")
		else:
			print("Wrong! Try again.")
