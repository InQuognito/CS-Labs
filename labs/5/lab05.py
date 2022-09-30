def get_school(card):
	if int(card[5]) == 1:
		return 'School of Computing and Engineering SCE'
	elif int(card[5]) == 2:
		return 'School of Law'
	elif int(card[5]) == 3:
		return 'College of Arts and Sciences'
	else:
		return 'Invalid School'

def get_grade(card):
	if int(card[6]) == 1:
		return 'Freshman'
	elif int(card[6]) == 2:
		return 'Sophomore'
	elif int(card[6]) == 3:
		return 'Junior'
	elif int(card[6]) == 4:
		return 'Senior'
	else:
		return 'Invalid Grade'

def character_value(checkChar):
	convertedChar = ord(checkChar) - 65
	return convertedChar

def get_check_digit(card):
	checkDigit = 0
	for index, value in enumerate(card[:5], 0):
		checkDigit += ((index + 1) * (ord(value) - 65))

	for index, value in enumerate(card[5:9], 5):
		checkDigit += ((index + 1) * int(value))

	checkDigit %= 10
	return checkDigit

def verify_check_digit(card):
	if len(card) != 10:
		return False, 'The length of the number given must be 10'
	for index, value in enumerate(card[0:5]):
		if (ord(value) - 65) not in range(0,26):
			return False, f'The first 5 characters must be A-Z, the invalid character is at {index} is {value}'
	if int(card[5]) not in range(1,4):
		return False, 'The sixth character must be 1 2 or 3'
	if int(card[6]) not in range(1,5):
		return False, 'The seventh character must be 1 2 3 or 4'
	for index, value in enumerate(card[7:10]):
		if int(value) not in range(10):
			return False, f'The last 3 characters must be 0-9, the invalid character is at {index} is {value}'
	checkDigit = get_check_digit(card)
	if checkDigit != int(card[9]):
		return False, f'Check Digit {card[9]} does not match calculated value {checkDigit}.'
	return True, ''

def check_card():
	print('Linda Hall')
	print('Library Card Check')
	print('==================================================\n')

	card = input('Enter Library Card ID. Hit Enter to Exit ==> ')

	if card == '':
		pass
	else:
		verified, error = verify_check_digit(card)

		if verified == False:
			print(error)
		else:
			print(f'The card belongs to a student in {get_school(card)}')
			print(f'The card belongs to a {get_grade(card)}')

			print()
			check_card()

if __name__ == '__main__':
	check_card()
