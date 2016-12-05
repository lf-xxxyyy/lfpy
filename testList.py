classmates = ['michael', 'bob', 'tom']
print (classmates)
print (len(classmates))
print (classmates[0])
print (classmates[1])
print (classmates[2])
print (classmates[len(classmates) -1])

print ('reverse')

print (classmates[-1])
print (classmates[-2])


classmates.append('adam')
print(classmates)
classmates.insert(1, 'jack')
print(classmates)

print(classmates.pop())
print (classmates)

print (classmates.pop(0))
print (classmates)

classmates[1] = 'xman'
print (classmates)


L = ['apple', 123, True]
print (L)
L2 = ['X1', L]
print (L2)
print(L2[1][1])

t = (1, 2)
print (t)

t1 = (1)
print (t1)

t11 = (1,)
print (t11)

t2 = (1, L2)
print (t2)
t2[1][1][2] = False
print (t2)
t2[1][1].append('changeable')
print(t2)



