class Node:
    def __init__(self,value):
        self.root = value
        self.left = None
        self.right = None

def preorder(node):

    if node == None:
        return

    print(node.root)
    preorder(node.left)
    preorder(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(preorder(root))
