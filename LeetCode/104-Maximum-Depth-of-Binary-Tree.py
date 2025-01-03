# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(level, tree):
            if not tree:
                return level

            if tree.left is None and tree.right is None:
                return level + 1
            else:
                if tree.left is None:
                    return dfs(level + 1, tree.right)
                elif tree.right is None:
                    return dfs(level + 1, tree.left)
                else:
                    return max(dfs(level + 1, tree.right), dfs(level + 1, tree.left))

        return dfs(0, root)
