class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def preorder(node):

    if node == None:
        return

    print(node.data)
    preorder(node.left)
    preorder(node.right)

def iterativepreorder(node):
    if node is None:
        return None

    stack = [root]
    result = []

    while stack:
        node = stack.pop()

        result.append(node.data)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)
    return result



root = Node(10)
root.left = Node(5)
root.right = Node(7)
root.left.left = Node(6)
root.left.right = Node(2)

preorder(root)
ans = iterativepreorder(root)
print(ans)