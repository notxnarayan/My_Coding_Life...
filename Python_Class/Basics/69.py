from multiprocessing import Process, Event
from time import sleep

def car(e, n):
    while True:
        e.wait()
        print(f"Car {n} moving")
        sleep(1)

def admin(e):
    while True:
        print("Red Light")
        e.clear()
        sleep(3)
        print("Green Light")
        e.set()
        sleep(3)

if __name__ == "__main__":
    e = Event()
    ps = []
    for i in range(3):
        p = Process(target=car, args=(e,i))
        ps.append(p)

    for i in ps:
        i.start()

    ad = Process(target=admin, args=(e,))
    ad.start()

    for i in ps:
        i.join()
