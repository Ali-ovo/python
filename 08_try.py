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



'''
try 尝试打开一个文件， 手动输入文件名
如果出现异常提示文件不存在，并且用写入模式打开创建文件
如果没有出现异常 将数据关闭
无论是否异常 关闭文件
'''

file_name = input("请输入文件名: ")
try:
    file = open(file_name, "r",encoding="utf-8")
except FileNotFoundError:
    print("文件不存在")
    file = open(file_name, "w",encoding="utf-8")
else:
    print(file.read())
finally:
    file.close()
