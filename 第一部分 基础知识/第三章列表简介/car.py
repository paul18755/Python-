# -*- coding: utf-8 -*-
# @Author: ywb
# @Date:   2019-04-20 16:28:36
# @Last Modified by:   ywb
# @Last Modified time: 2019-04-20 16:44:28

#实现对列表的排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
a = sorted(cars)
print(a)
print(cars)
cars.reverse()
print(cars)
print(len(cars))