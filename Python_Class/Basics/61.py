import time
import os
from multiprocessing import Pool

def square(n):
    print(f'process {os.getpid()} {n}')
    n = n.upper()
    time.sleep(1)
    return n

if __name__ == '__main__':
    l = ['apple', 'pear', 'kiwi', 'banana', 'fig']
    with Pool(processes=3) as pool:
        result = pool.map(square, l)
    print(result)
