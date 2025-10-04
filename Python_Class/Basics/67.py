from multiprocessing import Process, Pipe

def worker_a(conn):
    numbers = [1, 2, 3, 4, 5]
    conn.send(numbers)
    conn.close()

def worker_b(conn):
    numbers = conn.recv()
    total = sum(numbers)
    print(f"Sum of {numbers} is {total}")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    p1 = Process(target=worker_a, args=(child_conn,))
    p2 = Process(target=worker_b, args=(parent_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
