def reversePolishNotation(tokens):
  stck = []
  for token in tokens:
    if token in ['-', '+', '*', '/']:
      a = stck.pop()
      b = stck.pop()
      stck.append(calculate(b,a,token))
    else:
      stck.append(token)
  return stck.pop()

def calculate(a, b, token):
  print(a, token, b)
  if token == '+':
    return int(a) + int(b)
  elif token == '-':
    return int(a) - int(b)
  elif token == '*':
    return int(a) * int(b)
  return int(a/b)

def evalRPN(tokens) -> int:
  operations = {
  "+": lambda a, b: a + b,
  "-": lambda a, b: a - b,
  "/": lambda a, b: int(a / b),
  "*": lambda a, b: a * b
  }

  stack = []
  for token in tokens:
    if token in operations:
      number_2 = stack.pop()
      number_1 = stack.pop()
      operation = operations[token]
      stack.append(operation(number_1, number_2))
    else:
      stack.append(int(token))
      return stack.pop()



print(reversePolishNotation(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))