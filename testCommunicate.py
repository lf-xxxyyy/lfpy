from multiprocessing import Process, Queue
import os, time, random

def write(q):
	print ('process to write: %s' % os.getpid())

	for val in range(10):
		q.put(val)
		time.sleep(random.random())

	for value in ['A', 'B', 'C']:
		print('put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	print('proces to read: %s' % os.getpid())
	while  True:
		value = q.get(True)
		print ('get %s from queue.' % value)


if __name__ == '__main__':
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))

	pw.start()
	pr.start()
	pw.join()
	pr.terminate()
