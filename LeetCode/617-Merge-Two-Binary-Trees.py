# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(base, node):
            if not node:
                return

            base.val += node.val
            
            if not base.left and node.left:
                base.left = TreeNode()
            if not base.right and node.right:
                base.right = TreeNode()

            dfs(base.left, node.left)
            dfs(base.right, node.right)

        if not root1 and root2:
            root1 = TreeNode()
        dfs(root1, root2)
        return root1