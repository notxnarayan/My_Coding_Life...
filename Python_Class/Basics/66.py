# 2.You need to write a Python program using multiprocessing.Semaphore where:
#
# There are 3 worker processes but only 2 resources are available at the same time.
#
# Use a semaphore to ensure that at most 2 workers can access the resource simultaneously.
#
# Each worker should print when it acquires and releases the resource.
import time
from multiprocessing import Semaphore,Process


def worker(sem,id):
    with sem:
        print(f"Acquired: {id}")
        time.sleep(5)
        print(f"Released: {id}")
if __name__ == "__main__":
    sem = Semaphore(2)

    workers = [Process(target=worker,args=(sem,i)) for i in range(0,3)]
    for i in workers:
        i.start()
    for i in workers:
        i.join()