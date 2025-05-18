class Student(object):
    def __init__(self, name, age, gender, mobile, des):
        self.name  = name
        self.age  = age
        self.gender  = gender
        self.mobile  = mobile
        self.des  = des
 
    def __str__(self):
        return f"姓名:{self.name}, 年龄:{self.age}, 性别:{self.gender}, 电话:{self.mobile}, 描述信息:{self.des}"


if __name__ == '__main__':
    s1 = Student('张三', 20, "男", "111131111", "爱好AI")
    print(s1)
    # 把对象的属性转成字典
    print(s1.__dict__)

    s2 = Student('李四', 21, "男", "111131111", "爱好AI2")
    print(s2)
    # 把对象的属性转成字典
    print(s2.__dict__)


