# -*- coding: utf-8 -*-
# @Author: ywb
# @Date:   2019-05-04 10:38:54
# @Last Modified by:   ywb
# @Last Modified time: 2019-05-04 11:17:48
with open('chapter_10/pi_digits.txt') as file_object:
		for line in file_object:
			print(line.rstrip())

with open('chapter_10/pi_digits.txt') as file_object:
		contents = file_object.read()
		print(contents.rstrip())

with open('chapter_10/pi_million_digits.txt') as file_object:
	lines = file_object.readline()
pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))

birthady = input('Enter your birthady, in the form mmddyy: ')
if birthady in pi_string:
	print('Your birthady appears in the first million digits of pi!')
else:
	print('Your birthday does not appear in the first million digiths of pi!')


with open('chapter_10/programming1.txt', 'w') as file_object:
	file_object.write('I Love programming.\n')
	file_object.write('I Love creating new games.\n')

with open('chapter_10/programming1.txt', 'a') as file_object:
	file_object.write('I also Love programming.\n')
	file_object.write('I also Love creating new games.\n')

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)



import json
numbers = [2,3,5,7,11,13]
filename = 'numbers.json'
with open(filename, 'a') as f_obj:
	json.dump(numbers,f_obj)

with open('numbers.json') as f_obj:
	numbers = json.load(f_obj)
print(numbers)




















