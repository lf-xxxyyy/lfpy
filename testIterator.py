from collections import Iterable

print (isinstance([], Iterable))

print (isinstance({}, Iterable))

print (isinstance((x * x for x in range(10)), Iterable))

print (isinstance(10, Iterable))

M = {'a':'x', 'b':'y'}
for k, v in M.items():
	print (k, '=', v)

def add(x, y , f):
	return f(x) + f(y)


print (add(-5, 6, abs))


def power(x):
	return x * x

print (add(-5, 6, power))

