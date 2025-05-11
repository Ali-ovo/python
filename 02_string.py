str1 = "single"
str2 = "double"
str3 = """triple"""
str4 = """
    quadruple
"""

str5 = """'''say: "I'm a student!"'''"""
print(str1, str2, str3, str4, str5)

print(len(str1), str1[0], str1[-1])


print(str1[0:3])
print(str1[0:5:2])
print(str1[::-1])  # reverse

print("in" in str1)


print(str1.find("in"), str1.find("g", 3), str1.find("e", 3, 6))

s1 = "hello python and java and js"
s2 = s1.replace("java", "c++")
s3 = s1.replace("and", "&&", 2)
print(s2)
print(s3)

s1 = "hello python and java and js"
s2 = s1.split(" ")
print(s2)

s1 = "hello python and java and js"
s2 = s1.split(" ", 2)
print(s2)

print(s1.count("a"))


s1 = "  text space  "
print(s1.strip())
print(s1.lstrip())
print(s1.rstrip())


list1 = ["a", "b", "c"]
print(" ".join(list1))


s1 = "Hello wORLD"
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.capitalize())
print(s1.title())


print(s1.startswith("H"))


s5 = "12"
print(s5.isdecimal())  # 最严格，只检查是否都是十进制数字字符 (0-9)
print(s5.isdigit())  # 较宽松，检查是否都是数字字符，包括十进制数字和上标/下标数字等
print(s5.isnumeric())  # 最宽松，检查是否都是数值字符，包括:
# "123": 三个函数都返回True
# "²": isdecimal()返回False，isdigit()返回True，isnumeric()返回True
# "½": 只有isnumeric()返回True
# "三": 只有isnumeric()返回True

s5 = "abc123"
print(s5.isalnum())  # 检查是否都是字母或数字字符
print(s5.isalpha())  # 检查是否都是字母字符
