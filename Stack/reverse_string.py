"""The program to reverse the string using the stack operations"""

from collections import deque


def is_empty(l):
    return len(l) == 0


string = input("Enter the string:")
list1 = deque()
for i in string:
    list1.append(i)
new_string = ""
while not is_empty(list1):
    new_string += list1.pop()
print(f"Reverse of the string is \"{new_string}\"")
