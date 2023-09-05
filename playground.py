class C:
    @classmethod
    def classsmethodss(cls):
        pass


print(bin(1212))
print(format(1212, "b"))


map1 = {
    1: "A",
    2: "B",
    3: "C",
}

print(map1.get(0, "Z"))
print(map1.pop("0", "Z"))
print(map1.popitem())

map2 = {4: "D"}

print(map1.update(map2))
map1 |= map2
print(map1)

arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]

print(arr.index(2, 5))

s = "Joonyoung Moon"

print(s.split("oo"), sep=";", end="\n")


from decimal import *

getcontext().prec = 3
getcontext().rounding = ROUND_HALF_UP

decimals = [Decimal(s) for s in "12 1234 234 .1 123.3".split()]

print(max(decimals))
print(min(decimals))
print(sum(decimals))
print([dec.exp() for dec in decimals])
print([dec.sqrt() for dec in decimals])
print([dec.ln() for dec in decimals])
print([dec.log10() for dec in decimals])


del arr[8:]
del arr[6:8:2]
print(arr.copy())
print(arr.insert(0, 0))
print(arr.remove(1))
print(arr.reverse())
print(arr)
arr.clear()

print(bin(1212))
print(format(1212, "b"))


def f(n):
    return n > 0


print(all(f(ans) for ans in [1, 2, 3, 4, 5, 6]))
print()

with open("text.txt", "r") as file:
    print(file.readlines())


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.isdisjoint(set2))
print(set2.issuperset(set2))
print(set1.issuperset(set2))
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
set1.update(set2)
set1.intersection_update(set2)
set1.difference_update(set2)
set1.symmetric_difference_update(set2)
set1.discard("1")
set1.pop()
print(set1.discard(0))


def f(a, b):
    return a > b


nums1 = [1, 2, 3, 4, 5]
nums2 = [2, 3, 4, 5, 6]

print(list(map(f, nums1, nums2)))
