def grep(pattern):
	while True:
		line = (yield)
		if pattern in line : 
			print (line)

g = grep('python')

g.send(None)

g.send('hello , python')

g.send('fuck')

g.send('hey, python')