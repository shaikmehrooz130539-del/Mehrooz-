import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

start = time.perf_counter()

sorted_arr = quick_sort(arr)

end = time.perf_counter()

print("\nSorted Array:", sorted_arr)
print("Execution Time:", end - start, "seconds")

print("\nTime Complexity")
print("Best Case  : O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case : O(n²)")