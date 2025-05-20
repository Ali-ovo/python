import time
import multiprocessing

my_list = []


def write_data():
    for i in range(3):
        my_list.append(i)
    print("write_data-->", my_list)


def read_data():
    time.sleep(0.2)
    print("read_data-->", my_list)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=write_data)
    p2 = multiprocessing.Process(target=read_data, daemon=True)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("my_list-->", my_list)
