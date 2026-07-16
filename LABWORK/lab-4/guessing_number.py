'''Problem 3: Number Guessing Game--------
 Create a number guessing game.
 Rules: 
• Secret number = 57  
• User gets only 7 attempts.  
• If the user enters a negative number, ignore it using continue.  
• If the user guesses correctly, terminate using break.  
• Display the number of attempts used'''

#----------------------------------------------------------------
#secret number:
secret = 57

attempt =0

while attempt <7:
     num = int(input("Enter your guess: "))
   if num <0:
    continue
 attempt += 1

#conditions:
    if num == secret:
        print("Correct Guess!")
        break
    elif num > secret:
        print("Too High")
    else:
        print("Too Low")
#printing the number of attempts:
print("Attempts Used:", attempt)
