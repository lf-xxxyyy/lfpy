import queue


class Task(object):
	taskid = 0
	def __init__(self, target):
		Task.taskid += 1
		self.tid = Task.taskid
		self.target = target
		self.sendval = None
	def run(self):
		return self.target.send(self.sendval)


class Scheduler(object):
	def __init__(self):
		self.ready = queue.Queue()
		self.taskmap = {}

	def new(self, target):
		newtask = Task(target)
		self.taskmap[newtask.tid] = newtask
		self.schedule(newtask)
		return newtask.tid

	def schedule(self, task):
		self.ready.put(task)

	def exit(self, task):
		print ("task %d terminated" % task.tid)
		del self.taskmap[task.tid]

	def mainloop(self):
		while self.taskmap:
			task = self.ready.get()
			try :
				result = task.run()
			except StopIteration:
				self.exit(task)
				continue
			self.schedule(task)



def foo():
	for i in range(10):
		print ("I'm foo")
		yield

def bar():
	for i in range(5):
		print ("I'm bar")
		yield


sched = Scheduler()
sched.new(foo())
sched.new(bar())
sched.mainloop()





















