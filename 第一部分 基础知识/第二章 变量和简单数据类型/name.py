# -*- coding: utf-8 -*-
# @Author: ywb
# @Date:   2019-04-19 15:43:53
# @Last Modified by:   ywb
# @Last Modified time: 2019-04-19 16:17:18

# 用引号引起来的都是字符串
a = 'I told my friend, "Python is my favorite language!"'
print(a)

# 修改字符串的大小写
b = 'ada lovelace'
print(b.title())
print(b.upper()) #全部大写
print(b.lower()) #全部小写

# 使用+合并字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")

#添加空白（\n \t）
print("\tpython")
print("languages:\nPython\nC\nJavaScript")

#删除空格
favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#Python之禅
import this
