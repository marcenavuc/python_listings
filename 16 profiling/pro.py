import cProfile
import time
import timeit

def fast():
    print("Я быстрая функция")
 
 
def slow():
    time.sleep(3)
    print("Я очень медленная функция")
 
 
def medium():
    time.sleep(0.5)
    print("Я средняя функция...")
 
 
def main():
    fast()
    slow()
    medium()
 
if __name__ == '__main__':
    # 1 спосооб
    start = time.time()
    main()
    end = time.time()
    print(end - start)

    # 2 способ
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(end - start)

    # 3 способ
    print(timeit.timeit("main()", number=1))

    cProfile.run("main()")
    # main()
