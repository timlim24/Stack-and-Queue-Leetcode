class Node:
    '''Represents a node in a singly linked list for stack storage.'''
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self) -> bool:
        return self.head is None

    def add(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None

        removed_data = self.head.val
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._size -= 1
        return removed_data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.val

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
