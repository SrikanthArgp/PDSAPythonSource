class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minstack) == 0 or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self) -> any:
        e = self.stack.pop()
        if e == self.minstack[-1]:
            self.minstack.pop()
        return e

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]

minSt = MinStack()
minSt.push(6)
minSt.push(8)
minSt.push(10)
minSt.push(4)
minSt.push(12)
minSt.push(6)

print(minSt.getMin())
print(minSt.pop())

