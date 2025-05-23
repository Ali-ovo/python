import re


def match_number(text):
    pattern = r"^\d+$"
    result = re.match(pattern, text)
    if result:
        print(result.group())
    else:
        print("匹配失败")


# match_number("123")


def search_number(text):
    pattern = r"\d+"
    result = re.search(pattern, text)
    if result:
        print(result.group())
    else:
        print("匹配失败")


# search_number("123abc")


def replace(text):
    pattern = r"a"
    result = re.sub(pattern, "b", text)
    print(result)


# replace("a123a")


result = re.match("ali[123abc]", "ali789")
result = re.match("ali[123abc]", "ali123")
# if result:
#   print(result.group())
# else:
#   print("匹配失败")


result = re.match(r"(qq):([1-9]\d{4,11})", "qq:123123")
print(result.group())
print(result.group(1))
print(result.group(2))


