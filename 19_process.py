import time
import multiprocessing
import os

def coding(num, name):
    for i in range(num):
        print(f"{name} is coding {i}")
        time.sleep(0.2)
    print(f"coding: process {os.getpid()}, process_id {multiprocessing.current_process().pid}, parent_process_id {os.getppid()}")


def music(name,num):
    for i in range(num):
        print(f"{name} is music {i}")
        time.sleep(0.2)
    print(f"music: process {os.getpid()}, process_id {multiprocessing.current_process().pid}, parent_process_id {os.getppid()}")

if __name__ == "__main__":
    # t1 = time.time()
    # coding()
    # music()
    # t2 = time.time()
    # print(f"time: {t2 - t1}")

    t1 = time.time()
    p1 = multiprocessing.Process(target=coding, name="p1", args=(10, "xiaoming"))
    p2 = multiprocessing.Process(target=music, name="p2", kwargs={"num": 10, "name": "honghong"})

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    t2 = time.time()

    print(f"time: {t2 - t1}")
