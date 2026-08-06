# Binary Search

n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Sort the array
arr.sort()

print("Sorted array:", arr)

key = int(input("Enter search element: "))

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at position:", mid + 1)
        found = True
        break

    elif arr[mid] < key:
        low = mid + 1

    else:
        high = mid - 1

if not found:
    print("Element not found")