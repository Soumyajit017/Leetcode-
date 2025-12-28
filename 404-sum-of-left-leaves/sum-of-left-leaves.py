# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        count = 0
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            count += root.left.val
        count += self.sumOfLeftLeaves(root.left)
        count += self.sumOfLeftLeaves(root.right)
        return count