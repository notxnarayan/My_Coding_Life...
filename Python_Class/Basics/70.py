import multiprocessing as mp
import random
import time
import random

def producer(shared_list, lock, produced_count, start_barrier, stop_event):
    start_barrier.wait()
    while not stop_event.is_set():
        num = random.randint(1, 100)
        with lock:
            shared_list.append(num)
            produced_count.value += 1
        time.sleep(0.1)
def consumer(shared_list, lock, consumed_count, start_barrier, stop_event):
    start_barrier.wait()
    while not stop_event.is_set():
        with lock:
            if shared_list:
                maxi = len(shared_list)
                num = shared_list.pop(random.randint(0,maxi-1))
                print(num**2)
                consumed_count.value += 1
        time.sleep(0.1)

if __name__ == "__main__":
    with mp.Manager() as manager:
        shared_list = manager.list()
        lock = mp.Lock()
        produced_count = mp.Value("i", 0)
        consumed_count = mp.Value("i", 0)
        num_producers = 2
        num_consumers = 2
        start_barrier = mp.Barrier(num_producers + num_consumers)
        stop_event = mp.Event()
        processes = []


        for i in range(num_producers):
            p = mp.Process(target=producer,
                           args=(shared_list, lock, produced_count,
                                 start_barrier, stop_event))
            processes.append(p)
        for i in range(num_consumers):
            c = mp.Process(target=consumer,
                           args=(shared_list, lock, consumed_count,
                                 start_barrier, stop_event))
            processes.append(c)

        for p in processes:
            p.start()

        time.sleep(5)
        stop_event.set()
        for p in processes:
            p.join()
        print("Final Report:")
        print(f"Total numbers produced: {produced_count.value}")
        print(f"Total numbers consumed: {consumed_count.value}")
        print(f"Numbers remaining in list: {len(shared_list)}")
