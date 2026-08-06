from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c=Counter(nums)
        for i in (c.values()):
            print("K", i)
            if i>1:
                return True
        return False

         