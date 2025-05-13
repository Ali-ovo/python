def add(a, b):
    return a + b


def sub(a, b):
    return a - b


print(add(1, 2))
print(sub(1, 2))

age = 18


def func1():
    """
    this is a function
    """

    return age


res = func1()
print(res)


def func2():
    global num1
    num1 = 100
    print(num1)


func2()
print(num1)


def func3():
    global num1
    num1 += 1  # num1 = 1 会被误认为是声明然后复制， 导致 num1 = num1 + 1 无法执行，所以需要 global 声明
    print(num1)


func3()


def func4():
    func3()
    func2()


print(func4())


def func5(a, b, c, d):
    print(a, b, c, d)


func5(1, 2, 3, 4)
func5(b=2, a=1, c=3, d=4)


def func6(*args, a, b, c=10):
    print(args)
    print(a, b, c)


func6(1, 2, 3, 4, a=1, b=2)


def func7(**kwargs):
    print(kwargs)


func7(a=1, b=2, c=3, d=4)


list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)
print(list1 is list2)  # False 因为 list1 和 list2 的地址不同
# is 判断的是地址， == 判断的是值

print(id(list1))
print(id(list2))
