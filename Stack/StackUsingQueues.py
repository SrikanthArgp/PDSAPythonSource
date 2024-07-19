class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        x = self.queue[-1]
        self.queue = self.queue[:-1]
        return x

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        if not self.queue:
            return True

st = MyStack()
for i in range(1,6):
    st.push(i)
# for i in range(5):
while not st.empty():
    print(st.pop())