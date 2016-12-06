d = {'michael':95, 'bob':75, 'tracy':85}
print(d['michael'])
print(d['bob'])

d['adam'] = 67
print(d)


print ('michael' in d )
print ('tony' in d )

print(d.get('bob', -1))
print (d.get('tony', -1))


s = set([5, 6, 7, 7, 1, 2, 3, 4, 4])
print (s)

s.add(10)
print(s)

s.remove(7)
print(s)

s2 = set([1, 4, 11])
print (s & s2)

print (s | s2)