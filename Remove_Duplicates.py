class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def remove_duplicates(head):

    if head is None:
        return None

    curr=head
    seen=set() #set() function is to remove the duplicate values from the list
    seen.add(curr.data)

    while curr.next:
        if curr.next.data in seen:
            curr.next=curr.next.next #skip the duplicats logic''
        else:
            seen.add(curr.next.data)
            curr=curr.next
    return head

def printList(head):
    while head is not None:
        print(f"{head.data}",end="->")
        head=head.next
    print("NULL")

if __name__=="__main__":
    head=Node(1)
    head.next=Node(1)
    head.next.next=Node(3)
    head.next.next.next=Node(3)
    head.next.next.next.next=Node(4)
    printList(head)
    head=remove_duplicates(head)
    printList(head)








