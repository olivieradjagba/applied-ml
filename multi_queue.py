# SuperFastPython.com
# example of using the queue with processes
from time import sleep, time
from random import random
from multiprocessing import Process
from multiprocessing import Queue

# generate work


def producer(queue):
    print('Producer: Running', flush=True)
    # generate work
    for i in range(100):
        # generate a value
        value = pow(i, 200)
        # block
        # sleep(value)
        # add to the queue
        queue.put(value)
    # all done
    queue.put(None)
    print('Producer: Done', flush=True)

# consume work


def consumer(queue):
    print('Consumer: Running', flush=True)
    # consume work
    while True:
        # get a unit of work
        item = queue.get()
        # check for stop
        if item is None:
            break
        # report
        print(f'>got {item}', flush=True)
    # all done
    print('Consumer: Done', flush=True)


# entry point
if __name__ == '__main__':
    st = time()
    for i in range(100):
        # generate a value
        value = pow(i, 200)
        # block
        # sleep(value)
        # add to the queue
        print(value)
    print(f'Simple done in {time()-st}s')
    # all done
    st = time()
    # create the shared queue
    queue = Queue()
    # start the consumer
    consumer_process = Process(target=consumer, args=(queue,))
    consumer_process.start()
    # start the producer
    producer_process = Process(target=producer, args=(queue,))
    producer_process.start()
    # wait for all processes to finish
    producer_process.join()
    consumer_process.join()
    print(f'Queue done in {time()-st}s')
