from multiprocessing import Pool
import time
import os

def square(n):
    print(f'process {os.getpid()} {n}')
    time.sleep(2)
    return n*n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    with Pool(processes=2) as pool:
        results = pool.map(square, numbers)
    print("squared numbers", results)
