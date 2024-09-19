"""The program to perform the queue operations"""

from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.appendleft(data)

    def dequeue(self):
        if Queue.is_empty(self):
            raise Exception("Queue is empty.")
        print(self.queue.pop())

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


q = Queue()
print(q.is_empty())
for i in range(5):
    q.enqueue(i)

print(f"Length of  the queue is {q.size()}")
for i in range(6):
    q.dequeue()
