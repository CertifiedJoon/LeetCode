ss = ["james", "John", "janE", "joon"]
ss.sort(key=str.lower, reverse=True)
print(ss)

mapped = {1: "a", 2: "b", 3: "c"}
print(mapped.get(4, "d"))
print(mapped.pop(4, "d"))
print(mapped.popitem())
print(mapped.update(mapped))
print(mapped | mapped)
mapped |= mapped

nums1 = [1, 2, 3, 4]
nums2 = [2, 3, 4, 5]


def is_greater(a, b):
    return a > b


print(list(map(is_greater, nums1, nums2)))


name = "   Joonyoung Moon   "

print(name.index("oo", 4))
print(name.isalnum())
print(name.isalpha())
print(name.isascii())
print(name.isdecimal())
print(name.isdigit())
print(name.islower())
print(name.isnumeric())
print(name.isupper())
print(name.lstrip())
print(name.removeprefix("Joonyoung"))
print(name.removesuffix("Moon"))
print(name.replace("oo", "00"))
print(name.split("oo"))
print(name.splitlines())
print(name.strip("wcmowz"))

ss.sort(key=str.lower)

print(ss)
