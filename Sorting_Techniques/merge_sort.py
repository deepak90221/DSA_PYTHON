def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # Recursively sort left half
    right = merge_sort(arr[mid:])  # Recursively sort right half

    merged = []
    i, j = 0, 0  # Pointers for left and right subarrays

    # Merge the two sorted halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged  # Return the sorted array

def printList(arr):
    for temp in arr:
        print(temp, end=" ")
    print()

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers: ").split()))
    sorted_arr = merge_sort(arr)  # Store the sorted list
    print("Sorted array:")
    printList(sorted_arr)
