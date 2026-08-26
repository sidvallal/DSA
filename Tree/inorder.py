class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def inorder(node):

    if node == None:
        return

    inorder(node.left)
    print(node.data)
    inorder(node.right)


root = Node(10)
root.left = Node(5)
root.right = Node(7)
root.left.left = Node(6)
root.left.right = Node(2)

inorder(root)