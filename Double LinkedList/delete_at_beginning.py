class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def delete_at_start(head,data):
    if head and head.next is None:
        return None
    new_head=head.next
    new_head.prev=None
    del head
    return new_head
def printDLL(head):
    curr=head
    while curr is not None:
        print(f"{curr.data}",end=" = ")
        curr=curr.next
    print("NULL")

def insert_at_first(head,data):
    newNode=Node(data)
    newNode.next=head
    if head:
        head.prev=newNode
    return newNode

if __name__=="__main__":
    head=None
    head=insert_at_first(head,4)
    head=insert_at_first(head,3)
    head=insert_at_first(head,2)
    head=insert_at_first(head,1)
    printDLL(head)
    print("-------------")
    head=delete_at_start(head,1)
    printDLL(head)