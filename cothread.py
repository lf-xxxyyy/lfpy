import asyncio
import queue
import threading

@asyncio.coroutine
def threaded(target):
	messages = queue.Queue()
	target.send(None)
	def run_target():
		while True:
			item = messages.get()
			if item is GeneratorExit:
				target.close()
				return
			else:
				target.send(item)

	threading.Thread(target=run_target).start()

	try:
		while True:
			item = (yield)
			messages.put(item)
	except GeneratorExit:
		messages.put(GeneratorExit)

