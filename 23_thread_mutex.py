import threading

g_num = 0
mutex = threading.Lock()


def sun_num1():
    mutex.acquire()

    for i in range(1000000):
        global g_num
        g_num += 1

    mutex.release()
    print("sun_num1-->", g_num)


def sun_num2():
    mutex.acquire()

    for i in range(1000000):
        global g_num
        g_num += 1

    mutex.release()
    print("sun_num2-->", g_num)


if __name__ == "__main__":
    t1 = threading.Thread(target=sun_num1)
    t2 = threading.Thread(target=sun_num2) 
    t1.start()
    t2.start()

    t1.join()
    t2.join()
