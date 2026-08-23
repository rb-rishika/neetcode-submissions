# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res= root.val

        def dfs(node):
            nonlocal res
            if not node: 
                return 0 #if node doesn't exist the path sum is 0
            maxLeft= dfs(node.left)
            maxRight= dfs(node.right)
            maxLeft= max(0,maxLeft)
            maxRight= max(0,maxRight)

            res= max(res, node.val + maxLeft+ maxRight)
            return node.val+ max(maxLeft, maxRight)

        dfs(root)
        return res
        