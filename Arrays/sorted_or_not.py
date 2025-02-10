def sorted_or_not(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return 0
    return 1
arr=list(map(int,input().split()))
print(sorted_or_not(arr))