class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset_fin=[]
        res=[]
        def dfs(idx):
            if idx>=len(nums):
                res.append(subset_fin.copy())
                return 
            subset_fin.append(nums[idx])
            dfs(idx+1)
            subset_fin.pop()
            dfs(idx+1)

        dfs(0)
        return res
        