print(abs(100))
print(abs(-20))

print(int("123"))
print(int(124))

print(hex(255))
print(hex(1000))


def my_abs(x):
	if x>=0:
		return x; 
	else :
		return -x;

print ("use my abs_function val=%d" % my_abs(-100))



def nop() :
	pass

print(nop())