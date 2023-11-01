class Queue:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        x = self.stack[0]
        self.stack.remove(x)
        return x

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

    def empty(self):
        return self.size() == 0


q = Queue()
q.push(7)
q.push(8)
q.push(9)
print(q.pop())
print(q.peek())
print(q.pop())
