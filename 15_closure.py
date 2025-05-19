def func01():
    print("func01")


def myframework(func_callback):
    print("myframework")
    func_callback()


def func_out(num1):
    a = 10

    def func_inner(num2):
        nonlocal a
        a = a + 20
        sum = num1 + num2 + a
        print(sum)

    return func_inner


func_out = func_out(10)
func_out(20)
