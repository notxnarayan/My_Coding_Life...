from multiprocessing import Process, Value, Lock
import time

def incrementer(counter, lock):
    for _ in range(10000):
        with lock:
            counter.value += 1
if __name__ == '__main__':
    count = Value('i', 0)
    lock = Lock()
    processes = []

    for i in range(2):
        p = Process(target=incrementer, args=(count, lock))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f'final counter value : {count.value}')
