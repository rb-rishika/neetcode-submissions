
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c1= Counter(nums)
        vals=sorted(c1.items(), key=lambda x:x[1], reverse=True)
        sorted_counts = dict(vals[:k])
        return list(sorted_counts.keys())