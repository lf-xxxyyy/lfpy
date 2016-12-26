try :
	f = open('/Users/Tony/Documents/workspace/scrapy/lfpy/testFile.py', 'r')
	print(f.read())
finally:
	if f:
		f.close()


with open('/Users/Tony/Documents/workspace/scrapy/lfpy/testFile.py', 'r') as f:
	for line in f.readlines():
		print(line.strip())


