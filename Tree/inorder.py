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
    
def inorderTraversal(root):
    stack = []
    result = []
    current = root

    while current or stack:

        # Go as far left as possible
        while current:
            stack.append(current)
            current = current.left

        # Process the node
        current = stack.pop()
        result.append(current.data)

        # Move to right subtree
        current = current.right

    return result


root = Node(10)
root.left = Node(5)
root.right = Node(7)
root.left.left = Node(6)
root.left.right = Node(2)

inorder(root)
ans = inorderTraversal(root)
print(ans)
