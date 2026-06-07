class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = 0

    def push(self, value: int) -> None:
        if len(self.stack) == 0 :
            self.min_ = value
        else :
            self.min_ = min(self.min_, value)
        self.stack.append(value)

    def pop(self) -> None:
        if len(self.stack) > 1 and self.min_ == self.stack[-1] :
            self.min_ = min(self.stack[:-1])
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()