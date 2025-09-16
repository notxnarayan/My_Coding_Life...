from multiprocessing import Process, Value, Lock
import time

def deposit(balance, lock, amount, times):
    for _ in range(times):
        with lock:
            balance.value += amount

def withdraw(balance, lock, amount, times):
    for _ in range(times):
        with lock:
            balance.value -= amount

if __name__ == '__main__':
    balance = Value('i', 100)
    lock = Lock()

    p1 = Process(target=deposit, args=(balance, lock, 10, 1000))
    p2 = Process(target=withdraw, args=(balance, lock, 10, 1000))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'Final balance: {balance.value}')
