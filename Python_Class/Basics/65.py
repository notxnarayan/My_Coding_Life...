from multiprocessing import Process, Queue
import time
import random

def producer(q):
    for i in range(5):
        time.sleep(random.random())
        item = f"Item-{i}"
        q.put(item)
        print(f"[Producer] Produced {item}")

    q.put(None)  # Sentinel to signal consumer to stop

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break  # Exit when producer signals end
        print(f"[Consumer] Consumed {item}")
        time.sleep(random.random())

if __name__ == "__main__":
    q = Queue()

    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Processing finished ✅")