def daily_temperatures(temperatures):
  answers = [0 for _ in range(len(temperatures))]
  search_stack = []
  for i in range(len(temperatures)):
    while search_stack and temperatures[i] > temperatures[search_stack[-1]]:
      j = search_stack.pop()
      answers[j] = i - j
    search_stack.append(i)
  return answers

print(daily_temperatures([30,40,50,60]))