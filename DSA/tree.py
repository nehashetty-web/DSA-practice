class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(10)

root.left = Node(5)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(7)

root = Node(10)

root.left = Node(5)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(7)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def preorder(root):
