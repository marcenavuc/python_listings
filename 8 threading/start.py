import threading
import time


class MyRunnable(threading.Thread):
    # lock = threading.Lock()
    event = threading.Event()
    event.set()

    def run(self):
        # # self.lock.acquire()
        # # print(threading.currentThread().name, self.lock.locked())
        # # with self.lock:
        # # with self.event:
        #     for i in range(100):
        #         # self.lock.acquire()
        #         # print(f"Hey! I am {threading.currentThread().name} from MyRunnable {time.thread_time()}")
        # if self.event.is_set():
        #     self.event.wait()
        # else:
        #     self.event.set()
        self.event.wait()
        self.event.clear()
        self.do_something()
        self.event.set()

    @staticmethod
    def do_something():
        for i in range(100):
            print(f"Hey! I am {threading.currentThread().name}\
             from MyRunnable {time.thread_time()}")

for _ in range(5):
    thread = MyRunnable()
    thread.start()
