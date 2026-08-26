class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def postorder(node):

    if node == None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data)

def postorderTraversal(root):
    if root is None:
        return []

    stack1 = [root]
    stack2 = []
    result = []

    while stack1:
        current = stack1.pop()
        stack2.append(current)

        if current.left:
            stack1.append(current.left)

        if current.right:
            stack1.append(current.right)

    while stack2:
        current = stack2.pop()
        result.append(current.data)

    return result

root = Node(10)
root.left = Node(5)
root.right = Node(7)
root.left.left = Node(6)
root.left.right = Node(2)

postorder(root)
ans = postorderTraversal(root)

print(ans)