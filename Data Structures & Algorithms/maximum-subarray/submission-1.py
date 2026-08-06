class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, totalSum=0, nums[0]

        for num in nums:
            
            if currSum<0:
                currSum=0
            currSum+=num
            totalSum=max(totalSum, currSum)
        return totalSum
        