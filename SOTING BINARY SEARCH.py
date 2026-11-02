# Binary Search of Unsorted Array
# CSE25106

arr = []

# Read number of elements
n = int(input("Enter no of elements: "))

# Read elements
for i in range(n):
    element = int(input("Enter the element: "))
    arr.append(element)

# Check whether the list is sorted
if arr == sorted(arr):
    print("\nThe input list is already sorted.")
else:
    print("\nThe input list is not sorted.")
    print("\nSorting the list...")
    arr.sort()

# Display sorted list
print("\nThe sorted list is:", arr)

# Read element to search
key = int(input("\nEnter element to search: "))


# Binary Search Function
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Perform binary search
result = binary_search(arr, key)

# Display result
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")
