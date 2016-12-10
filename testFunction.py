def my_abs(x):
	if not isinstance(x, (int, float)) :
		raise TypeError('bad operand type')
	if x>=0:
		return x; 
	else :
		return -x;


def my_hello(x):
	return 'hello %s' % x


def power(x, n=2):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if not isinstance(n, (int)) :
		raise TypeError('bad operand type')

	s = 1 
	while n > 0 :
		s = s * x
		n = n - 1
	return s

def enroll(name, gender) :
	print ('name:', name)
	print ('gender:', gender )


def add_end(L=[]) :
	L.append("END")
	return L

def calc(numbers):
	sum = 0
	for num in numbers:
		sum = sum + num * num
	return sum


def fact(n):
	if n == 1 : 
		return 1
	else :
		return n * fact(n - 1)