import threading
import time


class MyThreading(threading.Thread):
	"""docstring for MyThreading"""
	def __init__(self, arg):
		super(MyThreading, self).__init__()
		self.arg = arg

	def run(self):
		x = 0
		global  id,a,lock
		while id<500:
			id = id+1
			lock.acquire()
			a += 1
			lock.release()
			print("currid is %d ,a:%d,time:%s" %  (id,a,self.name))


		# print("mythreading end id is %d ,time:%s" %  (id,self.name))


id = 0

a = 0

lock = threading.Lock()

def main():
	for x in range(1,50):
		t1 = MyThreading(999)
		t1.start()

if __name__ == '__main__':
	main()
		