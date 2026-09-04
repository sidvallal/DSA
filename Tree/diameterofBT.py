class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.maxi = 0

    def check(self, root):

        if root is None:
            return 0

        lh = self.check(root.left)

        rh = self.check(root.right)

        self.maxi = max(self.maxi, lh + rh)

        return 1 + max(lh, rh)

    def diameterOfBinaryTree(self, root):

        self.maxi = 0
        self.check(root)

        return self.maxi


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


solution = Solution()

answer = solution.diameterOfBinaryTree(root)

print("Diameter:", answer)
