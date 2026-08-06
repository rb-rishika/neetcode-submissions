from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts= Counter(nums)
        
        
        revCounts= dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
        print("RE", revCounts)
        return list(revCounts.keys())[0:k]