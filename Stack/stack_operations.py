"""The program to perform the stack operation on deque libray"""
from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peak(self):
        return self.stack[-1]

    def len(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


collection = Stack()
for i in range(5):
    collection.push(i)
print("Push successfully")
print(f"peek of the stack is {collection.peak()}")
print(f"Length of the stack is {collection.len()}")
for i in range(5):
    print(collection.pop())
