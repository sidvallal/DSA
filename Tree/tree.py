class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(7)
root.left.left = Node(6)
root.left.right = Node(2)


    #     10
    #     /\
    #    5  7
    #   /\
    #  6  2