class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def traverse(head):
    curr=head
    while curr:
        print(curr.data,end="<->")
        curr=curr.next
    print("NULL")

def insert_at_beginning(head,data):
    newNode=Node(data)
    newNode.next=head
    if head:
        head.prev=newNode
    return newNode

if __name__=="__main__":
    head=None
    head=insert_at_beginning(head,4)
    head=insert_at_beginning(head,5)
    head=insert_at_beginning(head,7)
    traverse(head)