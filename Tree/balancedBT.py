class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def check(self, root):

        if root is None:
            return 0

        lh = self.check(root.left)
        rh = self.check(root.right)

        if lh == -1 or rh == -1 or abs(lh - rh) > 1:
            return -1

        return 1 + max(lh, rh)

    def BalancedBT(self, root):

        ans = self.check(root)

        if ans == -1:
            return False

        return True


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.BalancedBT(root))

