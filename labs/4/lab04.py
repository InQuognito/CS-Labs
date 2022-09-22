########################################################################
##
## CS 101 Lab
## Program #4
## Name: Patrick Cotter
## Email: pccmmn@umsystem.edu
##
## PROBLEM : The player should be able to
##
## ALGORITHM :
##	  1. The program asks the user how many chips they would like to play with.
##	  1. The program asks the user how many chips they would like to wager for this round.
##
## ERROR HANDLING:
##	  The program loops in every input space in order to ensure a correct input value is given. The program cannot proceed until these checks pass.
##
## OTHER COMMENTS:
##	  Any special comments
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
	''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
	playAgain = 'idk' # Set input to an invalid option to enter the loop
	while (playAgain.lower() not in ['y','yes','n','no']): # Loops until a valid input is given
		playAgain = input('Do you want to play again? ==> ') # Get input
		if playAgain.lower() in ['y','yes']: # If the player wants to play again
			return True
		elif playAgain.lower() in ['n','no']: # If the player does not want to play again
			return False
		else: # If neither of the above options
			print('Invalid input! Please Try again') # Returns error message

def get_wager(bank : int, spins) -> int:
	''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
	print('You are playing with', bank, 'chips!')
	print(f'Welcome to round {spins}!')
	wager = 0 # Set input to an invalid option to enter the loop
	while (wager <= 0) or (wager > bank): # Loops until a valid input is given
		wager = int(input('How many chips do you want to wager? ==> ')) # Get input
		if (wager <= 0): # If the amount is too low
			print('Wager amount must be more than 0.') # Returns error message
		elif (wager > bank): # If the amount is too high
			print('Wager amount cannot be more than you own.') # Returns error message
	return wager

def get_slot_results() -> tuple:
	''' Returns the result of the slot pull '''
	reel1 = random.randint(1,10) # Generates a random number between 1 and 10.
	reel2 = random.randint(1,10) # Generates a random number between 1 and 10.
	reel3 = random.randint(1,10) # Generates a random number between 1 and 10.
	return (reel1, reel2, reel3)

def get_matches(reel1,reel2,reel3) -> int:
	''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike '''
	if (reel1 == reel2):
		if (reel1 == reel3):
			matches = 3
		else:
			matches = 2
	elif (reel2 == reel3):
		if (reel2 == reel1):
			matches = 3
		else:
			matches = 2
	elif (reel1 == reel3):
		if (reel1 == reel2):
			matches = 3
		else:
			matches = 2
	else:
		matches = 0
	return matches

def get_bank() -> int:
	''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
	bank = 0 # Set input to an invalid option to enter the loop
	while (bank < 1) or (bank > 100): # Loops until a valid input is given
		bank = int(input('How many chips do you want to play with? ==> ')) # Get input
		if (bank < 1): # If the amount is too low
			print('Chip amount must be more than 0.') # Returns error message
		elif (bank > 100): # If the amount is too high
			print('Chip amount must be no more than 100.') # Returns error message
	return bank

def get_payout(wager, matches):
	''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
	if matches == 3:
		return (wager * 10)
	elif matches == 2:
		return (wager * 3)
	else:
		return (wager * -1)

def slots():
	print('====================')
	print('Welcome to the Slot Machine!')

	bank = get_bank() # Gets the amount of chips for the user to play with
	initialBank = bank
	maxBank = bank
	spins = 0
	while (bank > 0):  # Program loops as long as the user has enough chips to continue
		spins += 1
		wager = get_wager(bank,spins) # Gets the amount of chips the user would like to wager

		reel1, reel2, reel3 = get_slot_results() # Generates three random numbers

		matches = get_matches(reel1, reel2, reel3) # Returns the amount of values that are matching
		payout = get_payout(wager, matches) # Returns the payout based on the amount of matching values
		bank += payout

		print('Your spin:', reel1, reel2, reel3)
		print('You matched', matches, 'reels')
		if payout < 0:
			print('You lost', payout)
		elif payout > 0:
			print('You won', payout)
		else:
			print('You didn\'t lose or gain anything.')
		print('Current bank:', bank)
		print()

		if bank > maxBank:
			maxBank = bank

	print('You lost your bank of', initialBank, 'chips in', spins, 'spins!')
	print('The most chips you had was', maxBank, '.')

if __name__ == "__main__":
	playing = True
	while playing:
		slots()
		playing = play_again()
		#print(playing)
