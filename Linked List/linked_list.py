"""The program to perform the linked list operations"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # """Function to add the element at the beginning of linked list"""
    def add_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        else:
            itr = Node(data, self.head)
            self.head = itr

    # """The function to print all the element in linked list"""

    def printer(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        itr = self.head
        while itr:
            print(itr.data, end="")
            itr = itr.next
            if itr:
                print("-->", end="")

    # The function to add the element at the end of linked list
    def add_end(self, data):
        if self.head is None:
            LinkedList.add_beginning(self, data)
            return
        itr = self.head
        while itr:
            if itr.next is None:
                itr.next = Node(data, None)
                break
            itr = itr.next

    # The function to remove the elements at the index of the linked list
    def remove_at_index(self, index):
        if index < 0 or index >= LinkedList.count_element(self):
            print("Can't remove element at that index.")
            return
        if index == 0:
            LinkedList.remove_beginning(self)
            return
        if index == LinkedList.count_element(self) - 1:
            LinkedList.remove_at_end(self)
            return
        itr = self.head
        count = 0
        while itr:
            if index == count + 1:
                itr.next = itr.next.next
                return
            count += 1
            itr = itr.next

    # The function to count number of elements in linked list
    def count_element(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    # The function add element at the index of linked list
    def add_index(self, index, data):
        if index < 0 or LinkedList.count_element(self) < index:
            print("The element can't add at that index")
            return
        elif index == 0:
            LinkedList.add_beginning(self, data)
            return
        elif index == LinkedList.count_element(self):
            LinkedList.add_end(self, data)
            return
        itr = self.head
        count = 0
        while itr:
            count += 1
            if count == index:
                temp = Node(data, itr.next)
                itr.next = temp
                return
            itr = itr.next

    # The function to remove the elements from the beginning of link list
    def remove_beginning(self):
        if self.head is None:
            print("Linked list is empty")
            return
        self.head = self.head.next

    # the function to remove the elements from the end of linked list
    def remove_at_end(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        itr = self.head
        while itr:
            if itr.next.next is None:
                itr.next = None
                break
            itr = itr.next


list1 = LinkedList()
list1.add_end(20)
list1.add_end(30)
list1.add_beginning(40)
list1.add_index(3, 50)
list1.add_index(1, 100)
list1.remove_at_index(2)
print(list1.count_element())
list1.printer()
