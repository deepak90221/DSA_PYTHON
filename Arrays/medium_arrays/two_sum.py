def teo_sum(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:

                return [i,j]
    return []
arr=list(map(int,input().split()))
target=int(input())
print(teo_sum(arr,target))