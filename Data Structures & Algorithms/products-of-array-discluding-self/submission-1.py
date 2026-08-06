class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        right=[1]*len(nums)
        prefix=1

        for i in range(0,len(nums)):
            left[i]*= prefix
            prefix*=nums[i]
        

        postfix=1
        for i in range(len(nums)-1, -1, -1):
            left[i]*=postfix
            postfix*=nums[i]
        print(left)
        return left