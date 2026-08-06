# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #BELOW is RECURSIVE SOLN
        # arr=[]

        # def dfs(node):
        #     if not node: 
        #         return
        #     dfs(node.left)
        #     arr.append(node.val)
        #     dfs(node.right)
        
        # dfs(root)
        # return  arr[k-1]

        #ITERATIVE

        stack=[]
        curr= root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
           #allowed to pop only when you have traversed
           #entire left side
            curr=stack.pop()
            k-=1
            if k==0:
                return curr.val
            curr=curr.right
            

        