"""the program to run the two thread back to back.It is serving and ordering thread"""

import threading
import time
from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.appendleft(data)

    def dequeue(self):
        if Queue.is_empty(self):
            raise Exception("Queue is empty.")
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


buffer = Queue()


def place_order(orders):
    for order in orders:
        buffer.enqueue(order)
        print(f"Place order of {order}")
        time.sleep(0.5)
    time.sleep(10)
    return place_order(orders)


def serve_order():
    while True:
        time.sleep(1)
        print(f"Item served is {buffer.dequeue()}")
        time.sleep(2)


if __name__ == '__main__':
    order = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    t1 = threading.Thread(target=place_order, args=(order,))
    t2 = threading.Thread(target=serve_order)

    t1.start()
    t2.start()
