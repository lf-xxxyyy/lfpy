print(sorted([36, 5, -12, 9, -21]))



def my_power(x):
	if x > 0 : 
		return x
	else :
		return -x

print(sorted([36, 5, -12, 9, -21], key = my_power))


print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse=True))


