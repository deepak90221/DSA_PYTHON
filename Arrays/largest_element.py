def largest_element(arr):
    max=arr[0]
    for num in arr:
        if num>max:
            max=num
    return max
arr=list(map(int,input().split()))
print(largest_element(arr))