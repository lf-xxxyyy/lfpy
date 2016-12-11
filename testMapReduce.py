from functools import reduce

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

print (reduce(add, [1,2,3,4,5,6]))

def my_cat(x, y):
	return x*10 + y

print (my_reduce(my_cat, [1,2,3,4,5,6,7]))

def char2num(s) :
	return {'0':0, '1':1,'2':2,'3':3,'4':4, '5':5,'6':6,'7':7,'8':8,'9':9}[s]


print (reduce(my_cat, my_map(char2num, '13579')))

print (reduce (lambda x, y : x*10 +y, map(char2num, '234234234')))







