from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c1=Counter(nums)
        return sorted(c1.items(), key=lambda item: item[1], reverse=True)[0][0]