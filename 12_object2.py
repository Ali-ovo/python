class Master(object):
    def __init__(self):
        self.kongfu = "古法煎饼果子配方"

    def make_cake(self):
        print(f"使用{self.kongfu}制作煎饼果子")


class School(object):
    def __init__(self):
        self.kongfu = "现代煎饼果子配方"

    def make_cake(self):
        print(f"使用{self.kongfu}制作煎饼果子")


class Prentice(School, Master):
    def __init__(self):
        self.kongfu = "猫氏煎饼果子配方"

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)
        # super(School, self).__init__()
        # super(School, self).make_cake()


student1 = Prentice()
student1.make_master_cake()
student1.make_school_cake()
student1.make_cake()


print(Prentice.__mro__)
