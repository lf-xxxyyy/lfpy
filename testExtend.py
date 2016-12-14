class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')

	def eat(self):
		print ('Eating meat...')

class Cat(Animal):
	def run(self):
		print('Cat is running...')


dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

a = list()
b = Animal()
c = Dog()

print (isinstance(a, list))
print (isinstance(b, Animal))
print (isinstance(c, Animal))

def run_twice(animal):
	animal.run()
	animal.run()

run_twice(dog)

run_twice(cat)

class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly...')

run_twice(Tortoise())


print (type(123))
print (type('sdfsdf'))
print (type(None))


print (type(abs))

print (type(123) == type(456))
print (type(123) == int)
print (type('abc') == type('123'))


print (isinstance((1,2,4), (list, tuple)))

print (dir())

print (len('ABC'))

print('abc'.__len__())

print ('ABC'.lower())









