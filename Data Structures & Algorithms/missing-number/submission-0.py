class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        xorr=n
        for i in range(len(nums)):
            #print(xorr, i,nums[i], i^nums[i],xorr^i^nums[i] )
            xorr=xorr^i^nums[i]
        return xorr

        