class Animal(object):
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
      
        print("小狗汪汪叫")
    def age(self):
      return 10

class Cat(Animal):
    def speak(self):
        print("小猫喵喵叫")
    def age(self):
      return 20
        
def make_noise(animal: Animal):
    animal.speak()
    
def get_max_age(dog: Dog, cat: Cat):
  if dog.age() > cat.age():
    return dog.age()
  else:
    return cat.age()
    
dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)

print(get_max_age(dog, cat))