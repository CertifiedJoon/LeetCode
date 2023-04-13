def is_happy(num: int) -> bool:
  set_visited = set()
  while num != 1:
    if num in set_visited:
      return False
    set_visited.add(num)
    num = sum_square_of_digits(num)
  return True

def sum_square_of_digits(num: int) -> int:
  ret = 0
  while num > 0:
    last_digit = num % 10
    num = num // 10
    ret += last_digit * last_digit
  return ret 

print(is_happy(2))