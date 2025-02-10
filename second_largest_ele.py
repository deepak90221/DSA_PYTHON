def second_largest(arr):
    arr=list(set(arr))
    arr.sort()
    return arr[-2] if len(arr)>1 else -1
arr=list(map(int,input().split()))
print(second_largest(arr))