import multiprocessing
import random
import time


def worker(n: int):
    sleep = random.randint(1, 10)
    time.sleep(sleep)
    print(f"I'm worker {n}, sleep {sleep}")


for i in range(5):
    process = multiprocessing.Process(target=worker, args=(i,))
    process.start()
