from decimal import *

getcontext().prec = 6
getcontext().rounding = ROUND_HALF_UP

print(list(map(Decimal, "12 123 2432.33 .34".split())))
