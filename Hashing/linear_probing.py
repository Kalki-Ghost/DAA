"""The program is linear probing in hashing."""
"""Linear probing is process of prevent the collision in hashing."""


def hash_key(key):
    ans = 0
    for i in key:
        ans += ord(i)
    return ans % 100


class Hash:
    def __init__(self):
        self.arr = [None for _ in range(100)]

    def add_element(self, key, element):
        h = hash_key(key)
        if self.arr[h] is None:
            self.arr[h] = (key, element)
        else:
            for i in range(len(self.arr)):
                if self.arr[i] is None:
                    self.arr[i] = (key, element)

    def remove_element(self, key):
        for i in range(len(self.arr)):
            if self.arr[i] is not None:
                if key in self.arr[i]:
                    self.arr[i] = None
                    return
        print("Key Not found")

    def search(self, key):
        h = hash_key(key)
        if self.arr[h] is None:
            print("Key not found")
        elif self.arr[h][0] == key:
            print(f"{key}:{self.arr[h][1]}")
        else:
            for i in range(len(self.arr)):
                if self.arr[i] is not None and self.arr[i][0] == key:
                    print(f"{key}:{self.arr[i][1]}")
                    return
            print("Key not found")

    def printer(self):
        print(self.arr)


array = Hash()
array.add_element("Nov 10", "Rashmi")
array.add_element("May 15", "Venkatesh K")
array.printer()
array.remove_element("Nov 15")
array.remove_element("May 15")
array.search("May 15")
array.search("Max 18")
array.printer()
