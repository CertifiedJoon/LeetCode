class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append((val, 1))
        elif val == self.minStack[-1][0]:
            self.minStack[-1] = (val, self.minStack[-1][1] + 1)
        elif val < self.minStack[-1][0]:
            self.minStack.append((val, 1))

        self.stack.append(val)

    def pop(self) -> None:
        if self.minStack[-1][0] == self.stack[-1]:
            self.minStack[-1] = (self.minStack[-1][0], self.minStack[-1][1] - 1)
            if self.minStack[-1][1] == 0:
                self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
