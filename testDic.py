d = {'michael':95, 'bob':75, 'tracy':85}
print(d['michael'])
print(d['bob'])

d['adam'] = 67
print(d)


print ('michael' in d )
print ('tony' in d )

print(d.get('bob', -1))
print (d.get('tony', -1))
