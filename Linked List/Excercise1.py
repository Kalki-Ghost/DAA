class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            itr = Node(data, self.head)
            self.head = itr

    def insert_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)

    def length(self):
        itr = self.head
        total = 0
        while itr:
            total += 1
            itr = itr.next
        return total

    def insert_index(self, index, data):
        if 0 > index > self.length():
            print("You can't add the element at index")
        elif index == 0:
            self.insert_beginning(data)
        elif index == self.length():
            self.insert_end(data)
        else:
            itr = self.head
            total = 0
            while itr:
                total += 1
                if total == index:
                    break
                itr = itr.next
            itr.next = Node(data, itr.next)

    def insert_after_value(self, after_data, data):
        itr = self.head
        while itr:
            if itr.data == after_data:
                itr.next = Node(data, itr.next)
                return
            itr = itr.next
        print("Element not found")

    def insert_values(self, elements):
        for i in elements:
            self.insert_end(i)

    def remove_by_value(self, data):
        itr = self.head
        itr1 = itr.next
        if itr.data == data:
            self.head = itr1
            return
        while itr1:
            if itr1.data == data:
                itr.next = itr1.next
                return
            itr = itr.next
            itr1 = itr1.next
        print("Value not found")

    def print(self):
        if self.head is None:
            print("List is empty")
        else:
            itr = self.head
            while itr:
                print(itr.data, end="")
                itr = itr.next
                if itr:
                    print("-->", end="")
            print()


ll = LinkedList()
ll.insert_values(["banana", "mango", "grapes", "orange"])
ll.print()
ll.insert_after_value("mango", "apple")  # insert apple after mango
ll.print()
ll.remove_by_value("orange")  # remove orange from linked list
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()
