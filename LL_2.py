class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
def getLength(head):
    length=0
    while head:
        length+=1
        head=head.next
    return length

def getMiddle(head):
    length = getLength(head)
    middle_index=length//2
    while middle_index:

        head=head.next
        middle_index-=1
    return head.data

def main():


    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)
#since the middle terms are 30,40 it prints the second element in the middle-list

    print(getMiddle(head))

if __name__ == "__main__":
    main()