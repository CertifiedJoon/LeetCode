from decimal import *

getcontext().prec = 6
getcontext().rounding = ROUND_HALF_UP
nums = list(map(Decimal, "1 23 4 32 54345.99 234.00".split()))
print(nums)
print(max(nums), min(nums), sum(nums))
print([num.exp() for num in nums])
print([num.sqrt() for num in nums])
print([num.ln() for num in nums])
print([num.log10() for num in nums])


import math

print(math.comb(5, 2))
print(math.perm(5, 2))

import heapq

heapq.heapify(nums)
print(nums)
print(heapq.nlargest(3, nums))

import re

reg = r"[a-zA-Z0-9]*"
print(re.search(reg, "adfsa-asdf"))
print(re.fullmatch(reg, "adfasdfa15"))
print(re.split(reg, "___jij___"))
print(re.findall(reg, "adsfa@#$!asdfa"))
