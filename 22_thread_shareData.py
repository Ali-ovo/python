import threading
import time

my_list = []


def write_data():
    for i in range(3):
        my_list.append(i)
    print("write_data-->", my_list)


def read_data():
    time.sleep(0.2)
    print("read_data-->", my_list)


if __name__ == "__main__":
    t1 = threading.Thread(target=write_data)
    t2 = threading.Thread(target=read_data)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("my_list-->", my_list)
