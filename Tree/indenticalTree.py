class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def identical(root1, root2):
    # Both trees are empty
    if root1 is None and root2 is None:
        return True

    # One tree is empty, the other isn't
    if root1 is None or root2 is None:
        return False

    # Check current node and recursively check subtrees
    return (
        root1.data == root2.data
        and identical(root1.left, root2.left)
        and identical(root1.right, root2.right)
    )


tree1 = Node(1)
tree1.left = Node(2)
tree1.right = Node(3)

tree2 = Node(1)
tree2.left = Node(2)
tree2.right = Node(3)

print(identical(tree1, tree2))