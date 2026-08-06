class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, num in enumerate(nums):
            comp=target-num
            if comp in seen:
                return [seen.get(comp),i]
            else:
                seen[num]=i
        return [0,1]