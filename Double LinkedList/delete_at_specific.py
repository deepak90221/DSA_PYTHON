class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
def delete_at_position(head,position):
    if head and head.next is None:
        return None
    if position<0:
        return head
    if position==0:
        if head.next:
            head.next.prev=None
        return head.next

    curr=head
    count=0 #count variable to find the node to delete.

    '''
    
    Nodes are inserted in reverse order (1 -> 2 -> 3 -> 4).
    head → [1] ↔ [2] ↔ [3] ↔ [4] → None
    (Each node has prev and next pointers.)

    Deleting Node at Position 2 (Node with 3)
    We traverse using count:

    count = 0 → current = 1
    count = 1 → current = 2
    count = 2 → current = 3 (Found the node to delete)
    
    '''

    while curr and count<position:
        curr=curr.next
        count+=1

    if curr is None:
        return head
    if curr.next:
        curr.next.prev=curr.prev
    if curr.prev:
        curr.prev.next=curr.next
    del curr
    return head

def traverse(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node


if __name__=="__main__":
    head = None
    head = insert_at_beginning(head, 4)
    head = insert_at_beginning(head, 3)
    head = insert_at_beginning(head, 2)
    head = insert_at_beginning(head, 1)

    head = delete_at_position(head, 2)

    traverse(head)