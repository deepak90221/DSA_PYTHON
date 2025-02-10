class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def last_to_firsts(head):
    if head is None or head.next is None:
        return head
    second_last=None
    last=head
    while last.next is not None:
        second_last=last
        last=last.next

    second_last.next=None
    last.next=head
    head=last
    return head


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


    printList(head)

    head = last_to_firsts(head)

    printList(head)
