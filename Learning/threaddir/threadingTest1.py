import threading
from time import sleep,ctime


loops = [4,2]

def loop(index,nsec):
	print('Start loop %d at %s' % (index,ctime()))
	sleep(loops[index])
	print('end loop %d at %s' % (index,ctime()))

def  main():

	threads = []

	for i in range(len(loops)):
		t = threading.Thread(target = loop,args=(i,loops[i]))
		# t.setDaemon(True)
		t.start()
		threads.append(t)
		print(t.name)


	for i in range(len(loops)):
		threads[i].join()

	for i in range(1,5):
		print (i)

if __name__ == '__main__':
	main()