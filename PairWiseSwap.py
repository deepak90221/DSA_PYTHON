class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def pair_wise_swap(head):
    if head is None or head.next is None:
        return head

    curr=head
    while curr and curr.next:
        #a,b=b,a
        curr.data,curr.next.data=curr.next.data,curr.data
        curr=curr.next.next
    return head

def printList(head):
    while head is not None:
        print(f"{head.data}",end="->")
        head=head.next
    print("NULL")

if __name__=="__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    printList(head)
    head=pair_wise_swap(head)
    printList(head)
