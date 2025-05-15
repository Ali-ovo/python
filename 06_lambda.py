def sum1(a, b):
    return a + b


print(sum1(1, 2))


sum1 = lambda a, b: a + b

print(sum1(1, 2))

list1 = [[3,4],[1,5],[8,7],[6,3]]
list1.sort(key=lambda x: x[0])
print(list1)


func1 = lambda *args: sum(args)
print(func1(1, 2, 3, 4, 5))

func3 = lambda a,b: a if a>b else b
print(func3(1,2))