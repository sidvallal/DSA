class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root, subRoot):

        # Check whether two trees are identical
        def sameTree(root1, root2):

            if root1 is None and root2 is None:
                return True

            if root1 is None or root2 is None:
                return False

            return (
                root1.val == root2.val
                and sameTree(root1.left, root2.left)
                and sameTree(root1.right, root2.right)
            )

        # Empty tree is a subtree
        if subRoot is None:
            return True

        # Root is empty, so subtree cannot exist
        if root is None:
            return False

        # Check if current tree matches subRoot
        if sameTree(root, subRoot):
            return True

        # Search left and right
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )


root = TreeNode(3)

root.left = TreeNode(4)
root.right = TreeNode(5)

root.left.left = TreeNode(1)
root.left.right = TreeNode(2)


subRoot = TreeNode(4)

subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)


solution = Solution()

result = solution.isSubtree(root, subRoot)

print(result)