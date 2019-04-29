# -*- coding: utf-8 -*-
# @Author: ywb
# @Date:   2019-04-29 10:27:09
# @Last Modified by:   ywb
# @Last Modified time: 2019-04-29 11:06:42
alien_o = {'color': 'green','point':5}
print(alien_o['color'])

new_points = alien_o['point']
print('You just earned ' + str(new_points) + ' points')

alien_o['x_position'] = 0
alien_o['y_position'] = 25
print(alien_o)

alien_o['color'] = 'yellow'
print(alien_o['color'])

del alien_o['point']
print(alien_o)

user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}
for key, value in user_0.items():
	print("\nKey: "+key)
	print("Value: "+value)

favorite_languages = {
	'jen': 'python',
	'sarah': 'C',
	'edward': 'ruby',
	'phil': 'python'
}
for name in favorite_languages.keys():
	print(name.title())

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll")

for language in set(favorite_languages.values()):
	print(language.title())


alien_1 = {'color':'green', 'point': 5}
alien_2 = {'color': 'red', 'point': 10}
alien_3 = {'color': 'yellow', 'point':15}
aliens = [alien_1,alien_2,alien_3]
for alien in aliens:
	print(alien)


for alien_number in range(30):
	new_alien = {'color':'green', 'point':5,'speed':'slow'}
	aliens.append(new_alien)
print("Total number of aliens: " + str(len(aliens)))


favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}
for name,languages in favorite_languages.items():
	print('\n' + name.title()+ "'s favorite language are: ")
	for language in languages:
		print("\t" + language.title())

users = {
	'aeinstein':{
		'first': 'albert',
		'last':'einstein',
		'location': 'princeton',
	},
	'mcurie':{
		'first': 'marie',
		'last':'curie',
		'location':'paris',
	},

}
for username, user_info in users.items():
	print('\nUsername: ' + username)
	full_name = user_info['first']+" " + user_info['last']
	location = user_info['location']
	print("\tFull name: "+full_name.title())
	print("\tlocation: " + location.title())


































