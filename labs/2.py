weights = {
	'labs' : 70,
	'exams' : 20,
	'attendance' : 10
}

print ('**** Welcome to the Lab grade calculator! ****\n')

name = input('Who are we calculating grades for? ==> ')
print()

labsGrade = int(input('Enter the Labs grade? ==> '))
if (labsGrade < 0):
	labsGrade = 0
	print('The Labs value should have been zero or greater. It has been changed to zero.\n')
elif (labsGrade > 100):
	labsGrade = 100
	print('The Labs value should have been 100 or less. It has been changed to 100.\n')
else:
	print()

examsGrade = int(input('Enter the Exams grade? ==> '))
if (examsGrade < 0):
	examsGrade = 0
	print('The Exams value should have been zero or greater. It has been changed to zero.\n')
elif (examsGrade > 100):
	examsGrade = 100
	print('The Exams value should have been 100 or less. It has been changed to 100.\n')
else:
	print()

attendanceGrade = int(input('Enter the Attendance grade? ==> '))
if (attendanceGrade < 0):
	attendanceGrade = 0
	print('The Attendance value should have been zero or greater. It has been changed to zero.\n')
elif (attendanceGrade > 100):
	attendanceGrade = 100
	print('The Attendance value should have been 100 or less. It has been changed to 100.\n')
else:
	print()

weightedGrade = ((weights['labs'] * labsGrade) + (weights['exams'] * examsGrade) + (weights['attendance'] * attendanceGrade)) / (weights['labs'] + weights['exams'] + weights['attendance'])
print(f'The weighted grade for {name} is {weightedGrade}')
if (0 <= weightedGrade < 60):
	print(f'{name} has a letter grade of F')
elif (60 <= weightedGrade < 70):
	print(f'{name} has a letter grade of D')
elif (70 <= weightedGrade < 80):
	print(f'{name} has a letter grade of C')
elif (80 <= weightedGrade < 90):
	print(f'{name} has a letter grade of B')
elif (90 <= weightedGrade <= 100):
	print(f'{name} has a letter grade of A')
print()

print ('**** Thanks for using the Lab grade calculator! ****')
