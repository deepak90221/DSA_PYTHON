def union_and_sort(arr1,arr2):
    c=list(set(arr1+arr2))
    c.sort()
    return c
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))


print(union_and_sort(arr1,arr2))