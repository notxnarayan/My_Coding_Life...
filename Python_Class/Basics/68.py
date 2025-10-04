from multiprocessing import Process,Pipe
def worker(conn):
    conn.send("hello from child process")
    msg = conn.recv()
    print(f"worker received msg is{msg}")
    conn.close()



if __name__=='__main__':

    parent_conn, child_conn = Pipe()
    p1= Process(target=worker,args=(child_conn,))
    p1.start()
    print(f"main received msg is",parent_conn.recv())
    parent_conn.send("hello back from main")


    p1.join()