from io import StringIO

f = StringIO()
f.write('hello')
f.write('   ')
f.write('world')

print(f.getvalue())

f = StringIO('hello\n  hi \n goodbye')
while True:
	s = f.readline()
	if (s == '') :
		break
	print(s.strip())

import os

print(os.name)
print(os.uname())
print(os.environ)
print('PATH', os.environ.get('PATH'))