list_num = [1, 2, 3, 4, 5]
print(list_num)
print(type(list_num))


# i = 0
# while i <= len(list_num) - 1:
#     print(list_num[i], end=":")
#     i += 1

# for i in list_num:
#     print(i, end=":")


list_num.append(6)
print(list_num)


list_num.insert(0, 0)
print(list_num)


list_num.pop()
print(list_num)


list_num.pop(0)
print(list_num)


list2 = ["a", "b", "c"]
list2.extend(list_num)
print(list2)

list2.remove("a")
print(list2)


# list2.clear()
# print(list2)


print(list2.count("b"))
print(list2.index("b"))
print("b" in list2)


list2.reverse()
print(list2)


del list2[-1]
print(list2)


list2.pop()
list2.sort()
print(list2)


list_num2 = [1, 2, 3, 3, 2, 1]
for i in list_num2:
    if i == 3:
        list_num2.remove(3)

print(list_num2)


list_num2 = [1, 2, 3, 3, 2, 1]
for i in list_num2[:]:  # 创建列表副本进行遍历
    if i == 3:
        list_num2.remove(i)
print(list_num2)


list3 = [1, 5, 3, 6, 4, 1]
list3.sort(reverse=True)
print(list3)


list4 = []
for i in range(1, 10):
    if i % 2 == 0:
        list4.append(i)
print(list4)


list5 = [f"this is {i}" for i in range(1, 10) if i % 3 == 0]
print(list5)



