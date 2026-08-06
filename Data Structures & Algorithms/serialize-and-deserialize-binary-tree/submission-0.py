# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=[]
        def dfs(node):
            if not node:
                res.append("N")
                return
            #preorder traversal
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #convert string back to array
        splitValues= data.split(',')
        i= 0
        def dfs():
            nonlocal i
            if splitValues[i]=="N":
                i+=1
                return 
            node= TreeNode(splitValues[i])
            i+=1
            node.left= dfs()
            node.right=dfs()
            return node
        return dfs()
