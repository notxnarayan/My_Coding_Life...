import time
import os
from multiprocessing import Pool

def square(n):
    print(f'process {os.getpid()} {n}')
    time.sleep(2)
    return n*n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    with Pool(processes=3) as pool:
        results = []
        for i in numbers:
            result = pool.apply_async(square, args=(i,))
            results.append(result)
        output = [res.get() for res in results]

    print("squared numbers", output)
