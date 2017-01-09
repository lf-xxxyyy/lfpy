def inner():
	coef = 1
	total = 0
	while True:
		try :
			input_val = yield			print(input_val)
			print (total)
			total = total + coef * input_val
		except Exception:
			return total


ii = inner()
ii.send(None)
ii.send(1)
ii.send(1)
ii.send(1)