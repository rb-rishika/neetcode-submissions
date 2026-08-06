class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def dfs(i, curr_list):
            if i==len(nums):
                res.append(curr_list[::])
                return 

            curr_list.append(nums[i])
            dfs(i+1,curr_list )
            curr_list.pop()

            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i+=1
                #leave current and move on, this is like moving left pointer to left 
                #in Three Sum
            dfs(i+1, curr_list)
        dfs(0, [])
        return res

        