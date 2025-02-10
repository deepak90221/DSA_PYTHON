'''
Here's a diagrammatic explanation of how the program works when adding 1 to the linked list 1 -> 9 -> 9 -> 9:

Initial Linked List
rust
Copy
Edit
1 -> 9 -> 9 -> 9
Step-by-Step Recursive Process
The function addOneToList starts at the head and recursively processes the linked list from the end to the beginning. Here's the step-by-step flow:

Base Case:

The recursion reaches the end of the list (head = None) and returns a carry of 1.
Processing the Last Node:

Node Data = 9, Carry = 1.
Add carry: 9 + 1 = 10.
Update the node value: 10 % 10 = 0.
Return new carry: 10 // 10 = 1.
Updated List:

rust
Copy
Edit
1 -> 9 -> 9 -> 0
Processing the Second-to-Last Node:

Node Data = 9, Carry = 1.
Add carry: 9 + 1 = 10.
Update the node value: 10 % 10 = 0.
Return new carry: 10 // 10 = 1.
Updated List:

rust
Copy
Edit
1 -> 9 -> 0 -> 0
Processing the Third Node:

Node Data = 9, Carry = 1.
Add carry: 9 + 1 = 10.
Update the node value: 10 % 10 = 0.
Return new carry: 10 // 10 = 1.
Updated List:

rust
Copy
Edit
1 -> 0 -> 0 -> 0
Processing the Head Node:

Node Data = 1, Carry = 1.
Add carry: 1 + 1 = 2.
Update the node value: 2 % 10 = 2.
Return new carry: 2 // 10 = 0 (no carry left).
Updated List:

rust
Copy
Edit
2 -> 0 -> 0 -> 0
Final Carry Handling
If there was still a carry after processing all nodes (e.g., if the list was 9 -> 9 -> 9), a new node would be created at the head with the carry value. However, in this case, the carry is 0, so no new node is added.
Final Linked List
rust
Copy
Edit
2 -> 0 -> 0 -> 0
Diagram Overview
Recursive Call Stack:

scss
Copy
Edit
addOneToList(Node(1)) -> addOneToList(Node(9)) -> addOneToList(Node(9)) -> addOneToList(Node(9)) -> Base case
Backtracking and Updating Nodes:

Carry propagates back through the recursion, updating the nodes from right to left.

'''
from webbrowser import open_new


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def addOneToList(head):
    # Base case: If we reach the end of the list, return carry = 1
    if head is None:
        return 1

    # Recursively add 1 to the next node
    carry = addOneToList(head.next)

    # Add the carry to the current node's data
    res = head.data + carry
    head.data = res % 10  # Update the current node with the last digit
    return res // 10  # Return the carry for the next node


def addOne(head):
    # Add 1 to the linked list
    carry = addOneToList(head)

    # If there's a leftover carry, create a new node
    if carry:
        newNode = Node(carry)
        newNode.next = head
        return newNode

    return head


def printList(head):
    while head is not None:
        print(f"{head.data}", end=" -> ")
        head = head.next
    print("NULL")


if __name__ == "__main__":
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(9)

    print("Original Linked List:")
    printList(head)

    head = addOne(head)

    print("\nLinked List After Adding One:")
    printList(head)

