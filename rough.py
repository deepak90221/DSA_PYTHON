class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_alternative(head):
    if head is None:
        return None
    curr = head
    while curr and curr.next:
        temp = curr.next
        curr.next = curr.next.next
        del temp
        curr = curr.next
    return head

def printList(head):
    while head is not None:
        print(f"{head.data}", end="->")
        head = head.next
    print("NULL")

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    print("Original List:")
    printList(head)
    delete_alternative(head)
    print("Modified List:")
    printList(head)
