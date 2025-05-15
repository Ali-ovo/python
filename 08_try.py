# NameError
# NameError: name 'a' is not defined
# print(a)

# TypeError
# TypeError: can only concatenate str (not "int") to str
# print("1" + 1)

# ValueError
# ValueError: invalid literal for int() with base 10: 'a'

# KeyError
# KeyError: 'a'
# dict = {"a": 1}
# print(dict["b"])

# IndexError
# IndexError: list index out of range
# list = [1, 2, 3]
# print(list[3])

try:
    print(10 / 0)
except ZeroDivisionError:
    print("除数不能为0")
except Exception as e:
    print(e)
else:
    print("没有异常")
finally:
    print("finally")
