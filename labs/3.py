import re
def guesser():
	print('Welcome to the Flarsheim Guesser!\n')

	print('Please think of a number between and including 1 and 100.\n')

	remainderOf3 = -1
	while (remainderOf3 < 0) or (remainderOf3 >= 3):
		remainderOf3 = int(input('What is the remainder when your number is divided by 3 ? ==> '))
		if remainderOf3 < 0:
			print('The value must be 0 or greater')
		elif remainderOf3 >= 3:
			print('The value must be less than 3')

	remainderOf5 = -1
	while (remainderOf5 < 0) or (remainderOf5 >= 5):
		remainderOf5 = int(input('What is the remainder when your number is divided by 5 ? ==> '))
		if remainderOf5 < 0:
			print('The value must be 0 or greater')
		elif remainderOf5 >= 3:
			print('The value must be less than 5')

	remainderOf7 = -1
	while (remainderOf7 < 0) or (remainderOf7 >= 7):
		remainderOf7 = int(input('What is the remainder when your number is divided by 7 ? ==> '))
		if remainderOf7 < 0:
			print('The value must be 0 or greater')
		elif remainderOf7 >= 3:
			print('The value must be less than 7')

	print(remainderOf3,remainderOf5,remainderOf7)

	for x in range (1,101):
		if remainderOf3 == (x % 3) and remainderOf5 == (x % 5) and remainderOf7 == (x % 7):
			print(x)

	print('How amazing is that?\n')
	playAgain = 'run'
	while playAgain != 'Y':
		playAgain = input('Do you want to play again? Y | N ==> ')
		if playAgain == 'Y':
			guesser()
		elif playAgain == 'N':
			break
		else:
			print('Options are \'Y\' and \'N\'.')

guesser()
