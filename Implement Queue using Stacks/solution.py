class Node:
    '''Represents a node in a singly linked list for stack storage.'''
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class Stack:
    '''A LIFO (Last-In-First-Out) Stack implementation using a linked list.'''
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, item):
        '''Adds an item to the top of the stack.'''
        self.head = Node(item, self.head)
        self.size += 1

    def pop(self):
        '''Removes and returns the item from the top of the stack.'''
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return val

    def peek(self):
        '''Returns the top item without removing it.'''
        val = self.head.val
        return val

    def is_empty(self):
        '''Checks if the stack is empty.'''
        return self.head is None

    def __len__(self):
        '''Returns the number of elements in the stack.'''
        return self.size

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
