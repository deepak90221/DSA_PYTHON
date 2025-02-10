# Linked List node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to set the middle node as the head of the linked list
def setMiddleHead(head):
    if head is None or head.next is None:  # Edge cases: empty list or single-node list
        return head

    # Initialize slow and fast pointers
    slow = head
    fast = head
    prev = None  # To keep track of the node before the middle

    # Traverse the list with slow moving one step and fast moving two steps
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        #fast moves two steps and travers until you get the last node


    # Set the middle node as the new head
    if prev:
        prev.next = slow.next  # Remove the middle node from its current position
    slow.next = head          # Set the next of the middle node to the original head
    head = slow               # Update the head to the middle node

    return head

# Function to insert a new node at the beginning of the list
def push(head, new_data):
    # Allocate new node
    new_node = Node(new_data)

    # Link the old list to the new node
    new_node.next = head

    # Move the head to point the new node
    head = new_node

    return head

# A function to print a given linked list
def printList(head):
    temp = head
    while temp:
        print(str(temp.data), end=" -> ")
        temp = temp.next
    print("NULL")

# Create a list of 5 nodes
head = None
for i in range(5, 0, -1):
    head = push(head, i)

print("List before:")
printList(head)

head = setMiddleHead(head)

print("\nList after setting middle as head:")
printList(head)
