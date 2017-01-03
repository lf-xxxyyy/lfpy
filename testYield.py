def h() :
	print ('before yield')
	yield 5 
	print ('after yield')

c = h()
c.next()


print('call next')
c.next()