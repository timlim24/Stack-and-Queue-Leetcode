class Stack:
    def __init__(self):
        self.items = []
    def push(self, x):
        self.items.append(x)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def is_empty(self):
        return len(self.items) == 0

class MyQueue:

    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()


    def push(self, x: int) -> None:
        self.stack_in.push(x)

    def pop(self) -> int:
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

        value = self.stack_out.pop()

        return value

    def peek(self) -> int:
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

        value = self.stack_out.pop()
        self.stack_out.push(value)

        return value


    def empty(self) -> bool:
        return self.stack_in.is_empty() and self.stack_out.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
