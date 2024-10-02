"""The program to Chaining method in hashing"""
"""Chaining is the process of prevent the collision in hashing."""


def hash_key(key):
    ans = 0
    for i in key:
        ans += ord(i)
    return ans % 100


class Hash:
    def __init__(self):
        self.arr = [[] for _ in range(100)]

    def add_element(self, key, element):
        h = hash_key(key)
        for i in range(len(self.arr[h])):
            if self.arr[h][i][0] == key:
                self.arr[h][i][1] = element
                return
        self.arr[h].append((key, element))

    def remove_element(self, key):
        h = hash_key(key)
        for i in range(len(self.arr[h])):
            if self.arr[h][i][0] == key:
                del self.arr[h][i]
                return
        print("Key not found")

    def search_element(self, key):
        h = hash_key(key)
        for i in range(len(self.arr[h])):
            if self.arr[h][i][0] == key:
                print(f"{key}:{self.arr[h][i][1]}")
                return
        print("Key not found")

    def printer(self):
        print(self.arr)


array = Hash()
array.add_element("Nov 10", "Rashmi")
array.add_element("Nou 11", "Ranjitha")
array.remove_element("Nou 11")
array.printer()
array.search_element("Nov 10")
array.search_element("May 15")
array.add_element("May 15", "Venkatesh K")
array.search_element("May 15")
array.printer()
