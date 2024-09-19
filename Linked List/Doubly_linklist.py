"""The program to perform the operation on  doubly linklist"""


class Node:
    def __init__(self, data, next, pre):
        self.data = data
        self.next = next
        self.pre = pre


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # The function to add the element at beginning
    def add_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            self.tail = self.head
            return
        itr = Node(data, self.head, None)
        self.head.pre = itr
        self.head = itr

    # The function to print the element from the front
    def front_printer(self):
        print("Front")
        if self.head is None:
            print("Linked list is empty.")
            return
        itr = self.head
        while itr:
            print(itr.data, end="")
            itr = itr.next
            if itr:
                print("-->", end="")
        print()

    # The function to print element from backward direction
    def back_printer(self):
        print("Back")
        if self.tail is None:
            print("Linked list is empty")
            return
        itr = self.tail
        while itr:
            print(itr.data, end="")
            itr = itr.pre
            if itr:
                print("-->", end="")
        print()

    # The function to return the number of elements in the linked list
    def counter(self):
        if self.head is None:
            return 0
        else:
            itr = self.head
            count = 0
            while itr:
                count += 1
                itr = itr.next
            return count

    # The function to add the element at the end of list
    def add_end(self, data):
        if self.head is None:
            LinkedList.add_beginning(self, data)
            return
        itr = Node(data, None, self.tail)
        self.tail.next = itr
        self.tail = itr

    # The function to add the element at particular index
    def add_at_index(self, index, data):
        if index < 0 or LinkedList.counter(self) < index:
            raise Exception("Can't add the element at this index.")

        if index == 0:
            LinkedList.add_beginning(self, data)
            return
        if index == LinkedList.counter(self):
            LinkedList.add_end(self, data)
            return

        itr = self.head
        count = 0
        while itr:
            count += 1
            if index == count:
                temp = Node(data, itr.next, itr)
                itr.next.pre = temp
                itr.next = temp
                return
            itr = itr.next

    # The function remove the element from the beginning of linked list
    def remove_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.pre = None

    # The function to remove the element at particular index of linked list
    def remove_at_index(self, index):
        if index < 0 or LinkedList.counter(self) < index:
            raise Exception("Can't remove the element at this index.")

        if index == 0:
            LinkedList.remove_beginning(self)
            return
        if index == LinkedList.counter(self) - 1:
            LinkedList.remove_end(self)
            return
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
            while index == count:
                itr.next.pre = itr.pre
                itr.pre.next = itr.next
                return

    # The function remove the element at the end of linked list
    def remove_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.pre
            self.tail.next = None


list1 = LinkedList()
list1.add_beginning(10)
list1.front_printer()
list1.add_beginning(20)
list1.front_printer()
list1.add_beginning(30)
list1.front_printer()
list1.back_printer()
list1.add_end(100)
list1.remove_beginning()
list1.remove_at_index(1)
list1.remove_at_index(1)
list1.remove_at_index(0)
list1.remove_at_index(1)
list1.back_printer()
list1.front_printer()
print(list1.counter())
