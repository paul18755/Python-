# -*- coding: utf-8 -*-
# @Author: ywb
# @Date:   2019-05-04 09:52:21
# @Last Modified by:   ywb
# @Last Modified time: 2019-05-04 10:29:29

class Dog():
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def sit(self):
		print(self.name.title() + ' is now siting.')
	def roll_over(self):
		print(self.name.title() + ' rolled over')

my_dog = Dog('willie', 6)
print('My dog`s name is ' + my_dog.name.title() + '.')
my_dog.sit()
my_dog.roll_over()

class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer(self):
		print('This car has ' + str(self.odometer_reading) + ' miles on it')
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print('You can not roll back an odometer!')

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 100
my_new_car.read_odometer()
my_new_car.update_odometer(300)
my_new_car.read_odometer()
my_new_car.update_odometer(200)


class Battery():
	def __init__(self, battery_size=70):
		self.battery_size = battery_size
	def describe_battery(self):
		print('This car has a ' + str(self.battery_size) + '-KWH battery.')
class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make,model,year)
		self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()



































