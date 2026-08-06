class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        maxLength=0

        for i in numSet:
            print(i)
            if i-1 not in numSet:
                length=0
                while (length+i) in numSet: 
                    length+=1
                maxLength= max(maxLength, length)

        return maxLength
        