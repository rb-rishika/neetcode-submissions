class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp=[false]*(len(nums))
        # dp[len(nums)-1]=true

        # for i in range(len(nums),1,-1):
        #     dp[i]=dp[i-1]

        goal= len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            print(nums[i], i, goal)
            if nums[i]+i>=goal: #"If I can get to stone 3, then I can eventually reach the end."
                goal=i
        return goal==0