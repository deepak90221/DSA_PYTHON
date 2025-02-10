class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.val)
        printInOrder(root.right)
def printPreOrder(root):
    if root:
        print(root.val)
        printPreOrder(root.left)
        printPreOrder(root.right)
def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.val)


root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.left.left = Node(4)

printInOrder(root)
print("------------")
printPreOrder(root)
print("------------")
printPostOrder(root)