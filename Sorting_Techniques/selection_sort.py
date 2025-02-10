def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # Find the minimum element
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the elements

def printList(arr):
    for temp in arr:
        print(temp, end=" ")
    print()

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    selection_sort(arr)
    printList(arr)
