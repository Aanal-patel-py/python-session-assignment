import time
import multiprocessing
import threading
from concurrent.futures import ThreadPoolExecutor

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 1.cpu bound task
def main():

    # normal
    x=1_000_000
    start=time.time()
    count=0
    for num in range(2, x+1):
        if is_prime(num):
            count+=1

    end=time.time()

    # multIthreading
    with ThreadPoolExecutor() as e:
        start1=time.time()
        list(e.map(is_prime, range(2, x+1))) #need to consume the result to ensure that the threads complete their execution as map is lazy and returns an iterator. If we don't consume the result, the threads may not execute at all.
        end1=time.time()

    # multiprocessing
        with multiprocessing.Pool() as p:
            start3=time.time()
            p.map(is_prime, range(2, x+1))
            end3=time.time()
        print(f"Time taken for multiprocessing execution: {end3 - start3} seconds")

    print(f"Time taken for normal execution: {end - start} seconds")
    print(f"Time taken for multithreading execution: {end1 - start1} seconds")

if __name__ == "__main__":
    main()