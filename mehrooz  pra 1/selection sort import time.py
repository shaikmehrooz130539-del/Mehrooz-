import time

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        minimum = i

        for j in range(i + 1, n):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[i], arr[minimum] = arr[minimum], arr[i]


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

start = time.perf_counter()

selection_sort(arr)

end = time.perf_counter()

print("\nSorted Array:", arr)
print("Execution Time:", end - start, "seconds")

print("\nTime Complexity")
print("Best Case  : O(n²)")
print("Average Case: O(n²)")
print("Worst Case : O(n²)")
print("Space Complexity: O(1)")