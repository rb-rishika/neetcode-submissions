class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #we have two pointers max and min to keep a track of 
        #negative and positive values. 
        res= nums[0]
        maxProd, minProd=1,1
        for num in nums:
            temp=maxProd*num
            maxProd= max(maxProd*num,minProd*num, num)
            minProd= min(temp,minProd*num, num)
            res=max(res, maxProd)
        return res
        