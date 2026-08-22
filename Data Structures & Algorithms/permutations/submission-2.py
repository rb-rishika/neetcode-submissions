class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res=[]
        visited=[False]*len(nums)
        def dfs(index, curr):
            if index==len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if visited[i]==True:
                    continue
                visited[i]= True
                curr.append(nums[i])
                dfs(index+1, curr)
                curr.pop()
                visited[i]= False                

        dfs(0,[])
        return res
        