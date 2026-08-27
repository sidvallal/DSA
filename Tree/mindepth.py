class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def depth(root):
    if root is None:
        return 0
    rl = depth(root.left)
    rr = depth(root.right)

    return 1 + min(rl,rr)

root = Node(10)
root.left = Node(5)
root.right = Node(7)
root.left.left = Node(6)
root.left.right = Node(2)

print(depth(root))


    #     10
    #     /\
    #    5  7
    #   /\
    #  6  2