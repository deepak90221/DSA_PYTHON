'''
Let's break it down in a very simple way to make it clear:

count % k == 0
This condition checks whether the current node's position (count) is a multiple of k. If it is, it means that the current node is the k-th node, and we need to delete it.

What is % (modulus operator)?
The modulus operator (%) gives the remainder when one number is divided by another.

Example:
5 % 2 = 1 (5 divided by 2 leaves a remainder of 1)
6 % 2 = 0 (6 divided by 2 has no remainder, so it's a multiple of 2)
10 % 3 = 1 (10 divided by 3 leaves a remainder of 1)
So, count % k == 0 means:

count is evenly divisible by k.
The current node is the k-th node in the sequence.
How It Works in the Program
Suppose k = 2 (delete every 2nd node):
Node Data	count	count % k	Is It k-th Node?
1	1	1 % 2 = 1	No
2	2	2 % 2 = 0	Yes (delete it)
3	3	3 % 2 = 1	No
4	4	4 % 2 = 0	Yes (delete it)
5	5	5 % 2 = 1	No
6	6	6 % 2 = 0	Yes (delete it)
Resulting List: 1 -> 3 -> 5

Suppose k = 3 (delete every 3rd node):
Node Data	count	count % k	Is It k-th Node?
1	1	1 % 3 = 1	No
2	2	2 % 3 = 2	No
3	3	3 % 3 = 0	Yes (delete it)
4	4	4 % 3 = 1	No
5	5	5 % 3 = 2	No
6	6	6 % 3 = 0	Yes (delete it)
Resulting List: 1 -> 2 -> 4 -> 5

Why It Matters in the Program
As we traverse the linked list, we increment a counter (count) for each node.
When count % k == 0, the program knows it has reached a k-th node and skips it (i.e., deletes it from the list).
Example Walkthrough:
Input List: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Let k = 2.

Start with count = 1:

Node 1: count = 1, count % 2 = 1 → Keep it.
Move to Node 2:

count = 2, count % 2 = 0 → Delete this node.
Move to Node 3:

count = 3, count % 2 = 1 → Keep it.
Move to Node 4:

count = 4, count % 2 = 0 → Delete this node.
Move to Node 5:

count = 5, count % 2 = 1 → Keep it.
Move to Node 6:

count = 6, count % 2 = 0 → Delete this node.
Final Output for k = 2:
Resulting list: 1 -> 3 -> 5

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_k(head, k):
    """
    Function to delete every k-th node in a linked list.
    :param head: The head node of the linked list.
    :param k: The position of the node to be deleted (1-based index).
    :return: The updated head of the linked list.
    """
    if not head or k <= 0:  # If the list is empty or k is invalid
        return head

    curr = head  # Pointer to traverse the list
    prev = None  # Pointer to track the previous node
    count = 1  # Position counter

    while curr:
        if count % k == 0:  # If the current node is the k-th node
            if prev:
                prev.next = curr.next  # Skip the current node
            # If it's not the head node
            else:
                head = curr.next  # Update head if the first node is deleted
        else:
            prev = curr  # Move the previous pointer only if no deletion occurs
        curr = curr.next  # Move to the next node
        count += 1

    return head


def print_list(head):
    """
    Function to print the linked list.
    """
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("NULL")


if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(5)
    head.next.next.next = Node(7)
    head.next.next.next.next = Node(11)
    head.next.next.next.next.next = Node(13)
    head.next.next.next.next.next.next = Node(15)
    head.next.next.next.next.next.next.next= Node(17)



    print("Original List:")
    print_list(head)

    k = 3
    head = delete_k(head, 3)  # Delete every k-th node

    print("List after deleting every 2nd node:")
    print_list(head)
