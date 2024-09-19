"""Arrays store the data in contiguous order. Store the data in RAM"""

arr = [298, 305, 320, 301, 292]
print(arr[2])  # Print the single value O(1)

for i in range(len(arr)):
    print(arr[i],end=' ')  # O(n)
print()
# Add the element to list
# arr.insert(1,280)
arr.append(280)
for i in range(len(arr)-1, 0, -1):
    arr[i] = arr[i - 1]
arr[1] = 280
print(arr)