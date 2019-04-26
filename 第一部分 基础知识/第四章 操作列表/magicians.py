# -*- coding: utf-8 -*-
# @Author: ywb
# @Date:   2019-04-20 16:50:35
# @Last Modified by:   ywb
# @Last Modified time: 2019-04-26 16:45:56
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
for value in range(1,5):
	print(value)
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
	squares.append(value**2) #**代表乘方运算
print(squares)

digits = range(1,11)
print(min(digits))
print('\n')
print(max(digits))
print('\n')
print(sum(digits))

# 提取列表的2到4个元素，将起始索引指定为1，终止索引指定为4
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
print(players[-3])

dimensions=(200,50)
print(dimensions[1])
for dimension in dimensions:
	print(dimension)
