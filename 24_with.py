# with open("1.txt", "w") as f:
#     f.write("hello world")


class MyFile(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("enter")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_value, traceback):
        print("exit")
        self.f.close()


if __name__ == "__main__":
    with MyFile("1.txt", "w") as f:
        f.write("hello world")
