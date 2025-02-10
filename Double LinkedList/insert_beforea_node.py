
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

def insert_before_node(node, data):
    if node is None:
        return

    new_node = Node(data)
    new_node.prev = node.prev
    new_node.next = node

    if node.prev:
        node.prev.next = new_node

    node.prev = new_node

head=Node(1)
node2=Node(2)
node3=Node(3)
head.next=node2
node2.prev=head
node2.next=node3
node3.prev=node2

traverse(head)


insert_before_node(node2,10)
traverse(head)


