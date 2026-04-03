class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def add(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

class MyStack:

    def __init__(self):
        self.queue_1 = Queue()
        self.queue_2 = Queue()


    def push(self, x: int) -> None:
        self.queue_2.add(x)
        while not self.queue_1.is_empty():
            self.queue_2.add(self.queue_1.pop())

        queue_1 = self.queue_1
        queue_2 = self.queue_2

        self.queue_1 = queue_2
        self.queue_2 = queue_1



    def pop(self) -> int:
        return self.queue_1.pop()

    def top(self) -> int:
        return self.queue_1.peek()

    def empty(self) -> bool:
        return self.queue_1.is_empty() and self.queue_2.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
