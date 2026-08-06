class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictPositions={}
        for i, num in enumerate(nums):
            if num in dictPositions:
                return True
            else: 
                dictPositions[num]=i
        return False

        