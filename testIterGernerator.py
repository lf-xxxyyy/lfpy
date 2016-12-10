import os

L = [x*x for x in range(1, 11)]
print (L)

print ([y*y for y in range(10 ,10)])

print ([x * x for x in range(10)])

print([m + n + x for m in 'ABC' for n in 'XYZ' for x in '123'])


print ([d for d in os.listdir('../')])

d = {'x':'a', 'y':'b', 'z':'c'}
for k, v in d.items():
	print (k, '=', v)



g = (x * x for x in range(10))

print (next(g))
print (next(g))


for n in g : 
	print (n)


for n in (x * x for x in range(10)):
	print (n)


def fib(max):
	n, a, b = 0, 0, 1
	while n < max : 
		yield b
		a, b = b, a +b
		n = n + 1

g = fib(10)

print (next(g))
print (next(g))
print (next(g))
print (next(g))
print (next(g))



def odd() :
	print('step 1')
	yield 1
	print ('step 2')
	yield 3
	print ('step 3')
	yield 5
	return 'haha'


o = odd()
print (next(o))
print (next(o))
print (next(o))
print (next(o))







