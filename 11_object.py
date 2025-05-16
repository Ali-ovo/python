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
      
car = Car("BMW", "红色")
car.run()
print(car)
del car