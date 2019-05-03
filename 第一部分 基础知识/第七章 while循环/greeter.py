# -*- coding: utf-8 -*-
# @Author: ywb
# @Date:   2019-05-03 14:58:18
# @Last Modified by:   ywb
# @Last Modified time: 2019-05-03 16:04:16
promot = 'If you tell us who you are, we can personalize the messages you see'
promot += '\nWhat is you name? '
name = input(promot)
print("\nHello, "+name +'!')

print(4%3)

number = input("Enter a number, and I`ll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
	print('\nThe number ' + str(number) + ' is even!')
else:
	print('\nThe number ' + str(number) + ' is odd!')

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ''
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)

active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print('Verifying user: ' + current_user.title())
	confirmed_users.append(current_user)
print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
	print(confirmed_user.title())


pets = ['dog', 'cat', 'dog', 'cat', 'goldfish', 'cat','rabbit','cat']
while 'cat' in pets:
	pets.remove('cat')
print(pets)














































