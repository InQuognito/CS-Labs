def character_value(checkChar):
	convertedChar = ord(checkChar) - 65
	return convertedChar

def get_check_digit(card):
    checkDigit = 0
    for inx, digit in enumerate(card[:5], 1):
        print(ord(digit) - 65)
        checkDigit += (inx + 1) * (ord(digit) - 65)
    print(checkDigit % 10)

    for inx, digit in enumerate(card[:5], 1):
        print(ord(digit) - 48)
        checkDigit += (inx + 1) * digit
    
    return checkDigit % 10

def check_name(id):
	for char in id[0:5]:
		if ord(id[char]) not in range(0,26):
			return False, char, chr(id[char])

def check_index_5(id):
	if ord(id[5]) not in range(1,4):
		return False

def check_index_6(id):
	if ord(id[6]) not in range(1,5):
		return False

def check_card():
	print('Linda Hall')
	print('Library Card Check')
	print('==================================================\n')

	card = input('Enter Library Card ID. Hit Enter to Exit ==> ')

	if len(card) != 10:
		print('ERROR: The length of the number must be 10.')
	condition, errorIndex, error = check_name(card)
	if condition == False:
		print(f'ERROR: The first 5 characters must be A-Z. The invalid character at {errorIndex} is {error}') # TODO: Return specific information about the invalid character.
	if check_index_5(card) == False:
		print('ERROR: The sixth character must be 1-3.') # TODO: Return specific information about the invalid character.
	if check_index_6(card) == False:
		print('ERROR: The seventh character must be 1-4.') # TODO: Return specific information about the invalid character.

if __name__ == '__main__':
	check_card()
