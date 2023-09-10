n = 257
n -= 1

print(bin(n))
n |= n >> 1

print(bin(n))
n |= n >> 2

print(bin(n))
n |= n >> 4

print(bin(n))
n |= n >> 8

print(bin(n))
n |= n >> 16

print(bin(n))
n |= n >> 32

n += 1

print(n)
