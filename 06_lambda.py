def sum(a, b):
    return a + b


print(sum(1, 2))


sum = lambda a, b: a + b

print(sum(1, 2))

list1 = [[3,4],[1,5],[8,7],[6,3]]
list1.sort(key=lambda x: x[0])
print(list1)