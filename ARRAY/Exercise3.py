"""Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function"""

num = int(input("Enter the range:"))
list1 = []
for i in range(1, num + 1):
    if i % 2 != 0:
        list1.append(i)
print(list1)
