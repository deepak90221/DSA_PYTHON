'''
Here’s a step-by-step explanation of how the insertion happens in a Doubly Linked List using a diagram representation.

Step 1: Initial Doubly Linked List
Before inserting the new node, our doubly linked list looks like this:

css
Copy
Edit
HEAD → [1] ⇄ [2] ⇄ [3] → None
Here:

⇄ indicates bidirectional links (prev and next).
Each node has two pointers: next (pointing to the next node) and prev (pointing to the previous node).
Step 2: Inserting a New Node (4) After Node 2
A new node 4 is created.
The new node's prev pointer is set to node 2.
The new node's next pointer is set to node 3.
Node 2's next pointer is updated to point to node 4.
Node 3's prev pointer is updated to point to node 4.
Step 3: Updated Doubly Linked List
After inserting node 4 after node 2, the list looks like this:

css
Copy
Edit
HEAD → [1] ⇄ [2] ⇄ [4] ⇄ [3] → None
Now, the pointers are:

Node 2.next → Node 4
Node 4.prev → Node 2
Node 4.next → Node 3
Node 3.prev → Node 4
Visual Representation of Pointers Before and After Insertion
Before Insertion
css
Copy
Edit
   [1] ⇄ [2] ⇄ [3]
    ↑      ↑      ↑
  head    node2   node3
After Insertion (Inserting 4 After Node 2)
scss
Copy
Edit
   [1] ⇄ [2] ⇄ [4] ⇄ [3]
    ↑      ↑      ↑      ↑
  head    node2  new    node3
                (4)
Code Breakdown
Creating Nodes:

python
Copy
Edit
head = Node(1)
node2 = Node(2)
node3 = Node(3)
head points to 1, node2 is 2, node3 is 3.
Linking the Initial Doubly Linked List:

python
Copy
Edit
head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
Establishes prev and next links.
Inserting Node 4 After Node 2:

python
Copy
Edit
insert_after_node(node2, 4)
Creates new_node = Node(4).
Updates new_node.prev = node2.
Updates new_node.next = node2.next (which is node3).
Updates node2.next = new_node.
Updates node3.prev = new_node.
Final Result
After insertion, the display() function prints:

rust
Copy
Edit
Doubly Linked List before insertion:
1 <-> 2 <-> 3 <-> None

Doubly Linked List after insertion:
1 <-> 2 <-> 4 <-> 3 <-> None
'''
from Tools.scripts.generate_re_casefix import hexint


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

def insert_at_beginning(node,data):
    if node is None:
        return
    newNode=Node(data)
    newNode.prev=node
    newNode.next=node.next
    node.next=newNode

head=Node(1)
node2=Node(2)
node3=Node(3)
head.next=node2
node2.prev=head
node2.next=node3
node3.prev=node2

traverse(head)


insert_at_beginning(node2,10)
traverse(head)


