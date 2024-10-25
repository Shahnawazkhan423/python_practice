# The program will keep asking for input.
# When the user inputs a negative number, the loop will stop.
# The program will output the sum of all positive numbers entered.
user=0
i=0
while user>=0:
    user = int(input('Enter The Positive Value:'))
    if user>=0:
        user+=user
        i+=1
print("Sum is:",user)
