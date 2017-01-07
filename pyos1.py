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


class SystemCall(object):
	def handle(self):
		pass

class GetTid(SystemCall):
	def handle(self):
		self.task.sendval = self.task.tid
		self.sched.schedule(self.task)
		print('hey, runing %d' % self.task.tid)


class NewTask(SystemCall):
	def __init__(self, target):
		self.target = target
	def handle(self):
		tid = self.sched.new(self.target)
		self.task.sendval = tid
		self.sched.schedule(self.task)

class KillTask(SystemCall):
	def __init__(self, tid):
		self.tid = tid
	def handle(self):
		task = self.sched.taskmap.get(self.tid, None)
		if task:
			task.target.close()
			self.task.sendval = True
		else :
			self.task.sendval = False
		self.sched.schedule(self.task)


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
				if isinstance(result, SystemCall):
					result.task = task
					result.sched = self
					result.handle()
					continue
			except StopIteration:
				self.exit(task)
				continue
			self.schedule(task)


def foo():
	mytid = yield GetTid()
	for i in range(10):
		print ("I'm foo, %d" % mytid)
		yield

def bar():
	mytid = yield GetTid()
	for i in range(5):
		print ("I'm bar, %d" % mytid)
		yield


def sometask():
	t1 = yield NewTask(bar())


def main():
	child = yield NewTask(foo())
	for i in range(10):
		yield
	yield KillTask(child)
	print ('main done')






sched = Scheduler()
sched.new(main())
sched.mainloop()



