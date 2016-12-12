
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

f = lazy_sum(1,2,3,4,5,6)

print(f)
print(f())


def my_lazy_sum(x, *args) :
	if x > 0:
		def sum():
			ax = 0
			for n in args:
				ax = ax + n
			return ax
		return sum
	else :
		def pw_sum():
			ax = 0 
			for n in args:
				ax = ax + n*n
			return ax
		return pw_sum


f2 = my_lazy_sum(1, 1,2,3,4,5,6)
print(f2)
print(f2())


f3 = my_lazy_sum(-1, 1,2,3,4,5,6,7)
print (f3)
print(f3())