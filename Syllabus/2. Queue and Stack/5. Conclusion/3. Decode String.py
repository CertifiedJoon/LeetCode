def decodeString(s):
  k_stk = []
  decode_stk = []
  for c in s:
    print(decode_stk, c)
    if c.isnumeric():
      k_stk.append(len(decode_stk))
      decode_stk.append(c)
    elif c == ']':
      k, ki = decode_stk[k_stk[-1]], k_stk.pop()
      decode_stk, encode_stk = decode_stk[:ki], decode_stk[ki + 1:]
      for _ in range(int(k)):
        decode_stk.extend(encode_stk)
    elif c != '[':
      decode_stk.append(c)
  return "".join(decode_stk)

print(decodeString("3[a2[c2[a]]ef]"))