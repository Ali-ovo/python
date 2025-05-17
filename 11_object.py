class Car:
    def run(self):
      print(f"车在跑： {self}”")
    def show(self):
      print(f"车的品牌是：{self.brand}，车的颜色是：{self.color}")
      
    def __init__(self, brand, color):
      self.brand = brand
      self.color = color
      
    def __str__(self) -> str:
      return f"车的品牌是：{self.brand}，车的颜色是：{self.color}"
      
    def __del__(self):
      print("车被销毁了")
      
# car = Car("BMW", "红色")
# car.run()
# print(car)
# del car


class Person(object):
  def __init__(self):
    self.name = "张三"
    self.sex = "男"
  
  def work(self):
    print("喜欢工作")
    
class Student(Person):
  def __init__(self):
    super().__init__()
    self.score = 90
    
  def study(self):
    print("喜欢学习")
    
student = Student()
student.work()
student.study()

class Student1(Student):
  def __init__(self):
    super().__init__()
    self.score = 100
    
  def study1(self):
    print("喜欢学习1")
    
student1 = Student1()
student1.work()
student1.study1()
student1.study()
