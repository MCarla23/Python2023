class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        x = self.stack[self.size() - 1]
        self.stack.remove(x)
        return x

    def peek(self):
        return self.stack[self.size() - 1]

    def size(self):
        return len(self.stack)

    def empty(self):
        return self.size() == 0


st = Stack()
st.push(7)
st.push(8)
st.push(9)
print(st.pop())
print(st.peek())
print(st.pop())