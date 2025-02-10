class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


def reverseList(head):
    prev=None
    curr=head

    while curr is not None:
        new_node=curr.next
        curr.next=prev
        prev=curr
        curr=new_node
    return prev

def printList(node):
    while node is not None:
        print(f"{node.data}", end="->")
        node = node.next
    print("NULL")


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    print("Original List:")
    printList(head)

    res = reverseList(head)

    print("Reversed List:")
    printList(res)
