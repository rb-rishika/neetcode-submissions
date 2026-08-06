class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        stack=[]

        def dfs(i, curr_sum):
            #base case
            if curr_sum==target:
                res.append(stack[:])
                return

            #out of bounds condition
            if curr_sum> target or i>=len(nums):
                return 
            
            #if we include curr elem
            stack.append(nums[i])
            dfs(i, curr_sum+ nums[i])
            stack.pop()

            #if not include:
            dfs(i+1, curr_sum)
            
    
        dfs(0,0)
        return res

        