class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, curr_sum):
            #Base:
            if i==len(nums):
                return 1 if curr_sum== target else 0
            return (
                dfs(i+1, curr_sum+nums[i]) #either add curr number or subtract
                + dfs(i+1, curr_sum-nums[i]))


        return dfs(0,0)


        