# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    csum = 0
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            self.csum += node.val
            node.val = self.csum
            dfs(node.left)
        
        dfs(root)
        return root