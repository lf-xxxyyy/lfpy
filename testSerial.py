import pickle

d = dict(name='bob', age=20, score=88)

print(pickle.dumps(d))

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()


d2 = dict(a = 'b')

f2 = open('dump.txt', 'rb')
d2 = pickle.load(f2)
f2.close()

print(d2)

import json
d3 = dict(name ='bob', age = 20, score = 88)

print(json.dumps(d3))

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

s = Student('Bob', 20, 88)

print(json.dumps(s, default=lambda obj: obj.__dict__))

