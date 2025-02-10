class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def delete_at_last(head):
    if head is None or head.next is None:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head

def printDLL(head):
    curr = head
    while curr is not None:
        print(f"{curr.data}", end=" <-> ")
        curr = curr.next
    print("None")

def insert_at_beginning(head, data):
    newNode = Node(data)
    newNode.next = head
    if head:
        head.prev = newNode
    return newNode

if __name__ == "__main__":
    head = None
    head = insert_at_beginning(head, 4)
    head = insert_at_beginning(head, 5)
    head = insert_at_beginning(head, 7)
    head = insert_at_beginning(head, 1)
    head = insert_at_beginning(head, 9)
    printDLL(head)
    print("___________________________")
    head = delete_at_last(head)
    printDLL(head)
