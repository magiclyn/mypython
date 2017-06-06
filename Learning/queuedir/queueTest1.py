from queue import Queue
from threading import Thread
from time import ctime,sleep

# A thread that produces data
def producer(out_q):
    a = 0
    while a<10:
        # Produce some data

        out_q.put(a)
        print(" put in a:%d" % a)
        a = a+1
        sleep(2)
    out_q.put(-1)

# A thread that consumes data
def consumer(in_q):
    while True:

        data = in_q.get()
        print('get data:%s' % data)
        sleep(1)

        if data == -1:
            in_q.task_done()
            print("in_q over")
            break
        in_q.task_done()


# Create the shared queue and launch both threads
q = Queue(2)
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()

# for i in range(10):
#     q.put(i,True)
#     print("put i%s" % i)
# q.put(-1)
q.join()

print("over")