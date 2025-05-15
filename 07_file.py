import os

# mode 读写模式 r 读 w 写 a 追加
# encoding 编码方式
# buffering 缓冲区
# newline 换行符
# closefd 是否关闭文件描述符
# opener 打开文件的方式
# file = open("1.txt", mode="r", encoding="utf-8")

# read(n) 可以指定读取的长度
# print(file.read())

# readline() 读取一行
# print(file.readline())

# readlines() 读取所有行 返回一个列表
# print(file.readlines())


# while True:
#     content = file.read(2)
#     if content == "":
#         break
#     print(content, end="")
# file.close()

# print("--------------------------------")
# file1 = open("1.txt", mode="w", encoding="utf-8")

# file1.write("one \n")

# file1.writelines(["床前明月光 \n", "疑是地上霜 \n", "举头望明月 \n", "低头思故乡"])

# file1.close()

# print("--------------------------------")


# file2 = open("1.txt", mode="a", encoding="utf-8")

# file2.write("\n hello")
# file2.close()

print(os.getcwd())
# os.rename("1.txt", "2.txt")

print(os.listdir())