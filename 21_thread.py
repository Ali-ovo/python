from threading import Thread, current_thread
import time


def coding(num, name):
    for i in range(num):
        print(f"{name} is coding {i}")
        time.sleep(0.2)


def music(name, num):
    for i in range(num):
        print(f"{name} is music {i}")
        time.sleep(0.2)
        
def get_thread_info():
    print(f"thread_id: {current_thread()}")

if __name__ == "__main__":
    time_start = time.time()
    t1 = Thread(target=coding, args=(10, "xiaoming"))
    t2 = Thread(target=music, args=("honghong", 10))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    time_end = time.time()
    print(f"time: {time_end - time_start}")
    
    
    for i in range(10):
        t = Thread(target=get_thread_info)
        t.start()
