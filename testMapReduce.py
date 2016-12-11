def f(x):
	return x * x

r = map (f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print (r)


def my_map(f, lst):
	ret_L = []; 
	for x in lst:
		ret_L.append(f(x))
	return ret_L

print (my_map (f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

print (my_map(str, [3, 4, 5, 6]))

def add(x, y):
	return x + y


def my_reduce(f, lst):
	n = 1
	rst = lst[0]
	while (n < len(lst)) :
		rst = f(rst, lst[n])
		n = n + 1
	return rst

print (my_reduce(add, [1,2,3,4]))

