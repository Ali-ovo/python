# tuple
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)

tuple2 = ()
print(tuple2)

tuple3 = 3
print(type(tuple3))

tuple4 = (3,)
print(type(tuple4))

tuple5 = 1, 2, 3, 4, 5
print(tuple5)

print(tuple5[0])
print(tuple5[-1])

# tuple5[0] = 100 # tuple can't be changed
# print(tuple5)

print(tuple5.index(5))
print(tuple5.count(5))


set1 = {1, 2, 3, 4, 5}
print(set1)

set1.add(6)
set1.add(6)
print(set1)

set2 = {True, 1, False, 0, 2.11}
print(set2)

dict1 = {"name": "小明", "age": 18}
print(dict1)

dict1["gender"] = "男"
print(dict1)
print(dict1["name"])
print(dict1.get("name"))
print(dict1.get("nickname", "default"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())

print(list(dict1.keys()))
print(list(dict1.values()))
print(list(dict1.items()))

dict1.update({"nickname": "小帅"})
dict1.update(height=180, width=100)
print(dict1)

dict1.pop("gender")
print(dict1)
dict1.popitem()
print(dict1)

for key, value in dict1.items():
    print(key, value)


print([1, 2, 3] + ["a", "b"])
print((1, 2, 3) + ("a", "b"))

print("123" * 3)
print([1, 2, 3] * 3)
print((1, 2, 3) * 3)


print(max(tuple1))
print(min(tuple1))
print(len(tuple1))
print(sum(tuple1))

print(any(tuple1)) # 只要有一个为真，就返回True
print(all(tuple1)) # 所有为真，才返回True







