class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_new={}
        for i in range(len(nums)):
            if nums[i] not in dict_new:
                dict_new[nums[i]]= i
            else:
                return True 
        return False
        