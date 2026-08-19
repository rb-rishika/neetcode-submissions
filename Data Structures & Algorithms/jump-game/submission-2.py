class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp=[false]*(len(nums))
        # dp[len(nums)-1]=true

        # for i in range(len(nums),1,-1):
        #     dp[i]=dp[i-1]

        goal= len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i>=goal:
                goal=i
        return goal==0