# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return 0
        q = deque()
        q.append(root)
        ans = []
        while q:
            level = len(q)
            sum_s = 0
            for _ in range(level):
                node = q.popleft()
                sum_s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(sum_s / level)
        return ans



        