class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newArr= nums[:]
        
        return list(nums+newArr)
        