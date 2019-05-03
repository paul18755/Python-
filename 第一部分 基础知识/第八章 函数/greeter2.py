# -*- coding: utf-8 -*-
# @Author: ywb
# @Date:   2019-05-03 21:21:47
# @Last Modified by:   ywb
# @Last Modified time: 2019-05-03 22:07:32
def greet_user(username):
	print("Hello, " + username.title()+'!')

greet_user('jesse') 

def describe_pet(pet_name, animal_type='hamster'):
	print('I have a '+animal_type)
	print('My ' + animal_type + "'s name is " + pet_name)
describe_pet('harry')

def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def greet_users(names):
	for name in names:
		print("Hello, " + name.title() + '!')
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

def make_pizza(*toppings):
	print("\nMaking a pizza with the following toppings")
	for topping in toppings:
		print('-' + topping)
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('yang','paul',location='princeton', field='physics')
print(user_profile)






















