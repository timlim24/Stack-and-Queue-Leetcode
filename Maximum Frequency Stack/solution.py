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

class FreqStack:
    def __init__(self):
        self.freqs = {}
        self.group_stacks = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val in self.freqs:
            self.freqs[val] += 1
        else:
            self.freqs[val] = 1

        freq = self.freqs[val]

        self.max_freq = max(self.max_freq, freq)

        if freq not in self.group_stacks:
            self.group_stacks[freq] = Stack()

        self.group_stacks[freq].push(val)

    def pop(self) -> int:
        target_stack = self.group_stacks[self.max_freq]
        val = target_stack.pop()

        self.freqs[val] -= 1

        if target_stack.is_empty():
            self.max_freq -= 1

        return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
