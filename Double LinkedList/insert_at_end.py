class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    new_node.prev = current
    return head

def display(head):
    current = head
    while current:
        print(f"{current.data}", end=" <-> ")
        current = current.next
    print(" ")

if __name__=="__main__":
    head = None
    head = insert_at_end(head, 1)
    head = insert_at_end(head, 2)
    head = insert_at_end(head, 3)

    display(head)