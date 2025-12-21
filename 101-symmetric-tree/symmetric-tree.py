# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric_tree(t1,t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            elif t1.val!=t2.val:
                return False
            else:
                return symmetric_tree(t1.left,t2.right) and symmetric_tree(t1.right,t2.left)
        return symmetric_tree(root.left,root.right)