def daily_temperatures_monotonic(temperatures):
  answers = [0 for _ in range(len(temperatures))]
  search_stack = []
  for i in range(len(temperatures)):
    while search_stack and temperatures[i] > temperatures[search_stack[-1]]:
      j = search_stack.pop()
      answers[j] = i - j
    search_stack.append(i)
  return answers

def daily_temperatures_top_down(temperatures):
  n = len(temperatures)
  hottest = 0
  answer = [0] * n

  for curr_day in range(n - 1, -1, -1):
    current_temp = temperatures[curr_day]
    if current_temp >= hottest:
      hottest = current_temp
      continue
    days = 1
    while temperatures[curr_day + days] <= current_temp:
      # Use information from answer to search for the next warmer day
      days += answer[curr_day + days]
      answer[curr_day] = days
    return answer

print(daily_temperatures_monotonic([30,40,50,60]))