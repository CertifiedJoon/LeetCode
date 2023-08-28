class C:
    @classmethod
    def f(cls, arg1, arg2):
        pass


def f(a):
    return a > 0


def f2(a, b):
    return a > b


nums = [12, 3, 4, 45, 2, -2]
nums2 = [1, 2, 3, 4, 5]
print(list(filter(f, nums)))

str_nums = ["+1.23", "   -1234\n", "1e-003", "-inf"]
print([float(num) for num in str_nums])

print([hex(num) for num in nums])

print(int("0110", 2))


def f2(a, b):
    return a > b


nums = [12, 3, 4, 45, 2, -2, 2]
nums2 = [1, 2, 3, 4, 5]

print(list(map(f2, nums, nums2)))

with open("text.txt", encoding="utf-8") as f:
    read_data = f.read()

print(*[12, 3, 4, 45, 2, -2], sep=" ", end="\n")

for num in reversed(nums):
    print(num, end=" ")

print("")

print(nums.index(2, 5))


del nums[:1]
print(nums)
del nums[1::2]
print(nums)
nums.clear()
print(nums)
nums.extend(nums2)
print(nums)
nums.insert(0, 0)
print(nums)
nums.remove(3)
print(nums)
nums.reverse()
print(nums)


nums.sort()


strings = ["aaaa", "bbbbb", "ccccccc"]
strings.sort(key=str.lower, reverse=True)
print(strings)

s = "joonyoung moon"
print(s.capitalize())

s = "joonyoung moon"
print(s.count("oo"))

sub = "oo"
print(s.find(sub, 1, 5))
print(s.isalnum())
print(s.isalpha())
print(s.isascii())
print(s.isdecimal())
print(s.isdigit())
print(s.islower())
print(s.isnumeric())
print(s.isupper())
print(s.lower())
print(s.lstrip())
print(s.removeprefix(sub))
print(s.removesuffix(sub))
print(s.replace("o", "0"))
print(s.rfind("m"))
print(s.split(" "))
print(s.splitlines())
print(s.strip("wcmowz."))

set0 = {1, 2, 3}
set1 = {1, 2, 3, 4, 5, 6}
set12 = {5, 6, 7, 8}
set2 = {7, 8, 9, 10, 11, 12}

print(set1.isdisjoint(set2))
print(set1.isdisjoint(set12))
print(set1.issuperset(set0))
print(set1.issubset(set12))
print(set1.union(set12, set2))
print(set1.intersection(set2))
print(set1.difference(set12))
print(set1.symmetric_difference(set12))
print(set1.update(set0))
print(set1.intersection_update(set12))
print(set1.symmetric_difference_update(set12))
print(set1.difference_update(set12))
print(set1.discard(1))

d = {"a": 1}
d["b"] = 2
d["c"] = 3

e = {"d": 4}

print(d.get("d", 0))
print(d.pop("d", 0))
print(d.popitem())
d.update(e)
print(d | e)
d |= e
