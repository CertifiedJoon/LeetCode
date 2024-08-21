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
