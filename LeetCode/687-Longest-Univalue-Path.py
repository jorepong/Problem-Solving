# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if not (node.left and node.left.val == node.val):
                left = 0
            if not (node.right and node.right.val == node.val):
                right = 0

            path_length = left + right
            self.longest = max(self.longest, path_length)

            return max(left, right) + 1

        dfs(root)
        return self.longest