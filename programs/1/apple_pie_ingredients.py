applePie = {
	'crusts' : 1,
	'apples' : 6,
	'sugar' : 0.75,
	'flour' : 2,
	'cinnamon' : 0.75,
	'salt' : 0.25,
	'nutmeg' : 0.125,
	'lemon' : 1
}

print('***APPLE PIE INGREDIENTS***\n')

pies = int(input('How many pies do you need ==> '))

if (pies == 1):
	print(f'\n\nFor {pies} pie you will need:\n')
else:
	print(f'\n\nFor {pies} pies you will need:\n')

ingredient = (applePie['crusts'] * pies)
if (ingredient <= 1):
	print(f'{ingredient} pie crust')
else:
	print(f'{ingredient} pie crusts')

ingredient = (applePie['apples'] * pies)
print(f'{ingredient} apples')

ingredient = (applePie['sugar'] * pies)
if (ingredient <= 1):
	print(f'{ingredient} cup of sugar')
else:
	print(f'{ingredient} cups of sugar')

ingredient = (applePie['flour'] * pies)
if (ingredient <= 1):
	print(f'{ingredient} tablespoon of flour')
else:
	print(f'{ingredient} tablespoons of flour')

ingredient = (applePie['cinnamon'] * pies)
if (ingredient <= 1):
	print(f'{ingredient} teaspoon of cinnamon')
else:
	print(f'{ingredient} teaspoons of cinnamon')

ingredient = (applePie['salt'] * pies)
if (ingredient <= 1):
	print(f'{ingredient} teaspoon of salt')
else:
	print(f'{ingredient} teaspoons of salt')

ingredient = (applePie['nutmeg'] * pies)
if (ingredient <= 1):
	print(f'{ingredient} teaspoon of nutmeg')
else:
	print(f'{ingredient} teaspoons of nutmeg')

ingredient = (applePie['lemon'] * pies)
if (ingredient <= 1):
	print(f'{ingredient} tablespoon of lemon juice')
else:
	print(f'{ingredient} tablespoons of lemon juice')
