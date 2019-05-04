# -*- coding: utf-8 -*-
# @Author: ywb
# @Date:   2019-05-04 11:31:57
# @Last Modified by:   ywb
# @Last Modified time: 2019-05-04 11:54:09
from name_function import get_formatted_name
print("Enter 'q' at any time to quit!")
while True:
	first = input('\nPlease give me a first name: ')
	if first == 'q':
		break
	last = input('Please give me a last name: ')
	if last == 'q':
		break
	formatted_name = get_formatted_name(first, last)
	print('\tNeatly formatted name: ' + formatted_name + '.')

import unittest
class NamesTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')
unittest.main()