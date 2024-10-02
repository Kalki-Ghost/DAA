"""The program to perform the hashing data type. Creating hash table by key given by user."""


def hashing(key):
    ans = 0
    for i in key:
        ans += ord(i)
    return ans % 100


class Hash:
    def __init__(self):
        self.arr = [None for _ in range(100)]

    def add_element(self, key, element):
        key = hashing(key)
        self.arr[key] = element

    def remove_element(self, key):
        k = hashing(key)
        element = self.arr[k]
        if element is None:
            print("Key not fond")
            return
        self.arr[k] = None
        print(f"{key}:{element} is removed")

    def search_element(self, k):
        key = hashing(k)
        element = self.arr[key]
        if element is None:
            print("Key not fond")
            return
        print(f"{k}:{element}")

    def printer(self):
        print(self.arr)


array = Hash()
array.add_element("march 6", 310)
array.add_element("march 7", 340)
array.add_element("march 8", 380)
array.add_element("march 9", 302)
array.add_element("march 10", 297)
array.add_element("march 11", 323)
array.printer()
array.search_element("march 9")
array.add_element("dec 30",88)
array.search_element("dec 30")
array.remove_element("march 6")
array.search_element("march 6")
