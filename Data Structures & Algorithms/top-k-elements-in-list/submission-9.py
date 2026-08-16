from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c1= Counter(nums)
        buckets=[[] for i in range(len(nums)+1)]
        res=[]

        for num,freq in c1.items():
            buckets[freq].append(num) 
        
        for bucket in range(len(buckets)-1,0,-1):
            if bucket:
                res.extend(buckets[bucket])

            if len(res)>=k:
                return res[:k]

        
        

        