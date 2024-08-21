class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        colderStack = []
        answer = [0 for _ in range(len(temperatures))]

        for i, temperature in enumerate(temperatures):
            while colderStack and colderStack[-1][1] < temperature:
                day, _ = colderStack.pop()
                answer[day] = i - day
            colderStack.append((i, temperature))

        return answer


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]

        if len(temperatures) < 2:
            return answer

        for i in range(len(temperatures) - 2, -1, -1):
            jump = 1
            start = i
            while temperatures[start + jump] <= temperatures[i]:
                if answer[start + jump] == 0:
                    break
                start += jump
                jump = answer[start]
            if temperatures[start + jump] <= temperatures[i]:
                answer[i] = 0
            else:
                answer[i] = start + jump - i

        return answer
