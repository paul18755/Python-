# -*- coding: utf-8 -*-
# @Author: ywb
# @Date:   2019-04-26 16:55:36
# @Last Modified by:   ywb
# @Last Modified time: 2019-04-26 17:06:22
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

#测试是否相等：
car = 'Audi'
if car.lower() == 'audi':
	print('Yes')
# 测试是否不相等 用!=
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies")
