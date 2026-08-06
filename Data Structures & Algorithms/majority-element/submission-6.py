class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter={}
        maxNumberOfTimes=0
        maxEl=nums[0]
        for i, num in enumerate(nums):
            if num in counter:
                counter[num]+=1
                if counter[num]> maxNumberOfTimes:
                    maxNumberOfTimes=counter[num]
                    maxEl=num
            else:
                counter[num]=1
        return maxEl
        