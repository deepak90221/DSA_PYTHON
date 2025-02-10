from collections import deque
class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x
def insertion_of_child(root,data):
    if root is None:
        root=Node(data)
        return root
    q=deque()
    q.append(root)

    while q:
        curr=q.popleft()
        if curr.left is None:
            curr.left=Node(data)
            return root
        else:
            q.append(curr.left)
        if curr.right is None:
            curr.right=Node(data)
            return root
        else:
            q.append(curr.right)

def InOrder(curr):
    if curr is None:
        return
    InOrder(curr.left)
    print(curr.data,end="  ")
    InOrder(curr.right)



if __name__=="__main__":
    root = Node(10)
    root.left = Node(11)
    root.right = Node(9)
    root.left.left = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(8)
    key=12
    root=insertion_of_child(root, key)
    InOrder(root)


