class Solution:
    def rob(self, nums: List[int]) -> int:
        #Base case
        if not nums:
            return 0 
        if len(nums)==1:
            return nums[0]
        skipLast = nums[0:len(nums)-1]
        skipFirst=  nums[1:len(nums)]

        return max(self.helper(skipLast), self.helper(skipFirst))
        
    def helper(self, nums: List[int]) -> int:    
       
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[1], nums[0])        
        for i in range(2,len(nums)):
            dp[i]= max(dp[i-1], nums[i]+dp[i-2])
        return dp[-1]
        