import re
def guesser(): # Defines the number guessing game in a function
	print('Welcome to the Flarsheim Guesser!\n')

	print('Please think of a number between and including 1 and 100.\n')

	remainderOf3 = -1 # Sets the remainder of 3 to an invalid input to enter the loop
	while (remainderOf3 < 0) or (remainderOf3 >= 3): # Loops until a valid input is given
		remainderOf3 = int(input('What is the remainder when your number is divided by 3 ? ==> ')) # Get input
		if remainderOf3 < 0: # Checking the bounds:
			print('The value must be 0 or greater') # Returns an error message and repeats the loop.
		elif remainderOf3 >= 3: # Checking the bounds:
			print('The value must be less than 3') # Returns an error message and repeats the loop.

	remainderOf5 = -1 # Sets the remainder of 3 to an invalid input to enter the loop
	while (remainderOf5 < 0) or (remainderOf5 >= 5): # Loops until a valid input is given
		remainderOf5 = int(input('What is the remainder when your number is divided by 5 ? ==> ')) # Get input
		if remainderOf5 < 0: # Checking the bounds:
			print('The value must be 0 or greater') # Returns an error message and repeats the loop.
		elif remainderOf5 >= 3: # Checking the bounds:
			print('The value must be less than 5') # Returns an error message and repeats the loop.

	remainderOf7 = -1 # Sets the remainder of 3 to an invalid input to enter the loop
	while (remainderOf7 < 0) or (remainderOf7 >= 7): # Loops until a valid input is given
		remainderOf7 = int(input('What is the remainder when your number is divided by 7 ? ==> ')) # Get input
		if remainderOf7 < 0: # Checking the bounds:
			print('The value must be 0 or greater')
		elif remainderOf7 >= 3: # Checking the bounds:
			print('The value must be less than 7') # Returns an error message and repeats the loop.

	for x in range (1,101): # Iterates loop for all possible numbers in the guessing game
		if remainderOf3 == (x % 3) and remainderOf5 == (x % 5) and remainderOf7 == (x % 7): # Checks every number against the three remainders the user gave. If all three match the current number, pass the check
			print(f'Your number was {x}') # Prints the correct guess

	print('How amazing is that?\n')
	playAgain = 'run' # Set input to an invalid option to enter the loop
	while playAgain != 'Y': # Loops until a valid input is given
		playAgain = input('Do you want to play again? Y | N ==> ') # Get input
		if playAgain == 'Y': # If the player wants to play again
			guesser() # Restarts the guessing game
		elif playAgain == 'N': # If the player does not want to play again
			break # Ends the loop, subsequently stopping the program
		else: # If neither of the above options
			print('Options are \'Y\' and \'N\'.') # Returns error message

guesser() # Runs the guessing game
