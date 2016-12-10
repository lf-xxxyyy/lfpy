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


