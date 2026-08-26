from collections import deque

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def BFS(node):
    if node is None:
        return None

    res = []
    queue = deque([root])

    while queue:

        node = queue.popleft()

        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

        

root = Node(10)
root.left = Node(5)
root.right = Node(7)
root.left.left = Node(6)
root.left.right = Node(2)

BFS(root)


    #     10
    #     /\
    #    5  7
    #   /\
    #  6  2