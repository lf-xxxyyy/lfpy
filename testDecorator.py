def log(func):
	def wrapper(*args, **kw) :
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper



@log
def now():
	print('2016-12-13')

now()



def hlog(text):
	def decorator(func):
		def wrapper(*arg, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*arg, **kw)
		return wrapper
	return decorator

@hlog('execute')
def now2():
	print('2016-12-14')

now2()


print(now2.__name__)