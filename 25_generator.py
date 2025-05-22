list = [i % 2 for i in range(10)]
print(list)

generator_list = (i % 2 for i in range(10))
print(generator_list)

print("===========")

# print(next(generator_list))


def generator(num):
    for i in range(num):
        print("start")
        yield i
        print("done")

# for i in generator(10):
#     print(i)

g = generator(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))