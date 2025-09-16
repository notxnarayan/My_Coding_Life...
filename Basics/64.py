from multiprocessing import Process, Value, Lock
import time

def increment(balance, lock, amount):
    while True:
        with lock:
            balance.value += amount
            time.sleep(0.5)

def decrement(balance, lock, amount):
    while True:
        with lock:
            balance.value -= amount
            time.sleep(0.5)

if __name__ == '__main__':
    balance = Value('i', 100)
    lock = Lock()
    inc_proc=[]
    dec_proc = []
    for i in range(0,10):
        p1 = Process(target=increment, args=(balance, lock,10))
        inc_proc.append(p1)

    for i in range(0,5):
        p2 = Process(target=increment, args=(balance, lock, 5))
        dec_proc.append(p2)



    for i in inc_proc:
        i.start()
    for i in dec_proc:
        i.start()


    while True:
        print(f'Final balance: {balance.value}')
