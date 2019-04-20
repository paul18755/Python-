# -*- coding: utf-8 -*-
# @Author: ywb
# @Date:   2019-04-19 16:25:38
# @Last Modified by:   ywb
# @Last Modified time: 2019-04-19 16:50:19
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# 提取列表的元素
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

# 修改列表
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 添加元素
motorcycles[0] = 'honda'
motorcycles.append('ducati')
print(motorcycles)
del motorcycles[0]
print(motorcycles) 

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles.remove('suzuki')
print(motorcycles)