'''
Example Breakdown
Initial Array:
plaintext
Copy
Edit
arr = [12, 11, 13, 5, 6]
First Iteration (i = 1)
python
Copy
Edit
i = 1
key = arr[i] = 11
j = i - 1 = 0
j starts at index 0, which is the position of 12.
Since 12 > 11, shift 12 to the right.
Second Iteration (i = 2)
python
Copy
Edit
i = 2
key = arr[i] = 13
j = i - 1 = 1
j starts at index 1, which is the position of 12.
Since 13 > 12, no shifting is needed.


-------------------------------------

Original array: [12, 11, 13, 5, 6]

Step 1: Insert 11 into sorted part [12]
Array after this step: [11, 12, 13, 5, 6]

Step 2: Insert 13 into sorted part [11, 12]
Array after this step: [11, 12, 13, 5, 6]

Step 3: Insert 5 into sorted part [11, 12, 13]
Array after this step: [5, 11, 12, 13, 6]

Step 4: Insert 6 into sorted part [5, 11, 12, 13]
Array after this step: [5, 6, 11, 12, 13]

Final Sorted Array: [5, 6, 11, 12, 13]

'''

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
def printList(arr):
    for temp in arr:
        print(temp,end=" ")

if __name__=="__main__":
    arr=list(map(int, input(). split()))
    insertion_sort(arr)
    printList(arr)
