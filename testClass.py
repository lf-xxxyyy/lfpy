class Student(object):
	
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s:%s'% (self.name, self.score))

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >=60:
			return 'B'
		else :
			return 'C'



bart = Student('bart simpson', 59)

print(bart.name)
print(bart.score)

print(bart.get_grade())

bart.print_score()

def print_score(std):
	print('%s : %s' % (std.name, std.score))


print_score(bart)


