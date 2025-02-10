def create_subStrings(str):
    n=len(str)
    for i in range(n):
        for j in range(i+1,n+1):
            print(str[i:j])
str=input("enter a string:")
print(create_subStrings(str))
