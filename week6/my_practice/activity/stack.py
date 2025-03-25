class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def is_empty(self):
        return not self.stack




stack = Stack()

stack.push(10000)
stack.push(12)
stack.push(80)
stack.push(5)


print(stack.stack)
stack.pop()
stack.pop()
print(stack.stack)
