# Linear Search

n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

key = int(input("Enter search element: "))

found = False

for i in range(n):
    if arr[i] == key:
        print("Element found at position:", i + 1)
        found = True
        break

if not found:
    print("Element not found")