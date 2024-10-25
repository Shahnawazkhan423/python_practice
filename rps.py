i=1
while i>=0:
	start = input("Enter Start And Exist:")
	if start == "start":
		user1 = input("Choose Any One Rock Paper and Scissors : ")
		user2 = input("Choose Any One Rock Paper and Scissors : ")
		if user1==user2:
			print("Match tie")
		elif user1 == "rock" and user2 == "scissors":
			print("Rock Win")
		elif user1 == "scissors" and user2 == "paper":
			print("Scissors Win")
		elif user1 == "paper" and user2 == "rock":
			print("Paper Win")
		elif user1 == "paper" and user2 == "scissors":
			print("Scissors Win")
		elif user1 == "scissors" and user2 == "rock":
			print("Rock Win")
		elif user1 == "rock" and user2 == "paper":
			print("Paper Win")
		else:
			print("Invalid Syntax")
	elif start=="exist":
		print("Exist The Game")
		break	
	else:
		print("Inavalid Value")