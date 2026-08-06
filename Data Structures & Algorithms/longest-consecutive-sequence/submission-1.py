class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums= set(nums)
        longest= 0
        for num in nums:
            if num-1 not in setNums:
                tempLongest=0
                while (num+tempLongest) in setNums:
                    tempLongest+=1
                longest=max(tempLongest,longest )
        return longest
        
"""
first- you try to see start of a subsequence by checking if the
left neighbor exists or not. If NOT, then you make it a start of a subsequence and 
compute right neigbours and append their length
"""