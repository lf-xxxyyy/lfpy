def is_odd(n):
	return n %2 == 1

print (filter(is_odd, [1,2,4,5,6,9,10,15]))



def not_empty(x):
	return x and x.strip()

print (filter(not_empty, 'a    b'))


def _odd_filter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x: x % n > 0

def primes() :
	yield 2
	it = _odd_filter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible, it)


for n in primes() :
	if n < 10000:
		print(n)
	else:
		break