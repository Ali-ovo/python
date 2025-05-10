age = 29

if age >= 18:
    print("你已經成年了")
elif age >= 13:
    print("你已經是青少年了")
else:
    print("你還未成年")

print(age if age >= 18 else "你還未成年")


i = 0
while i < 100:
    if i == 5:
        i += 1
        continue

    print(i)
    i += 1

    if i == 10:
        break


for i in "zhifuchuan":
    print(i, end=" ")

print()

for i in range(10, 0, -2):
    print(i, end=" ")
# 10 8 6 4 2
