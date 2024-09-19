"""The program to print the binary sequence of number"""

from collections import deque

queue = deque()


# The function to add the element to queue
def enqueue(data):
    queue.appendleft(data)


# The function to remove the element from the queue
def dequeue():
    return queue.pop()


# The function to return the last element of the queue
def first():
    return queue[-1]


enqueue("1")
num = int(input("Enter the number:"))
for i in range(num):
    f = first()
    print(f)
    enqueue(f + "0")
    enqueue(f + "1")
    dequeue()
