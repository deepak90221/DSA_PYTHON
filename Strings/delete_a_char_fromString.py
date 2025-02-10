'''
#using built-in function:

def remove_char(str,pos):
    if pos<0 and pos>len(str):
        return str
    return str[:pos] +str[pos:]
str=input()
pos=int(input())
print(remove_char(str,pos))'''

#own method

def remove_char(str,pos):
    if pos<0 and pos>len(str):
        return str
    str_list=list(str)
    #suppose you have aabbab in a string (" ") it will convert it into [ 'a','a','b','b','a','b'] for making it ease to delete
    for i in range(1,len(str)-1):
        str_list[i]=str_list[i+1] #pushes a string to the end and then deletes it....
    str_list.pop()

    return ' '.join(str_list) #this will covert to a string back from a list


if __name__=="__main__":
    str=input("enter the string : ")
    pos=int(input("enter the position to delete : "))
    print(remove_char(str,pos))