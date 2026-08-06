from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        queue.append(root)
        result=[]

        if not root: return []
        while queue:
            qlen= len(queue)
            level=[]
            for i in range(qlen):
                curr=queue.popleft()
                level.append(curr.val)
                if curr.left: 
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if level: 
                result.append(level)
                print(level)
        return result