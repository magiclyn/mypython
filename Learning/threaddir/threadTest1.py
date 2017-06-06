from time import sleep,ctime
import _thread

def loop0(lock):
	print('Start loop 0 at: %s' % ctime())
	sleep(2)
	lock.release()
	print('Loop 0 done at: %s' % ctime())

def loop1(lock):
	print('Start loop 1 at: %s' % ctime())
	sleep(2)
	lock.release()
	print('Loop 1 done at: %s' % ctime())

def main():
	print('start at:%s' % ctime())

	locks = []

	for i in range(2):
		lock = _thread.allocate_lock()
		lock.acquire()
		locks.append(lock)

	_thread.start_new_thread(loop0,(locks[0],))
	_thread.start_new_thread(loop1,(locks[1],))

	for  i in range(2):
		while locks[i].locked():
			pass

	print('all done at %s' % ctime())

if __name__ == '__main__':
	main()