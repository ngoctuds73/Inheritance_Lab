class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        return self.data.append(str(value))

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __repr__(self):
        return f"[{', '.join(reversed(self.data))}]"

asd = Stack()
[asd.push(x) for x in range(1, 9)]
print(asd)