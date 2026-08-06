class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c1= Counter(nums)
        seenList={}
        res=[]
        for i in range(len(nums)):
            if nums[i] in seenList:
                seenList[nums[i]]+=1
            else:
                seenList[nums[i]]=1
        
        vals=sorted(seenList.items(), key=lambda x:x[1], reverse=True)
        sorted_counts = dict(vals[:k])
        return list(sorted_counts.keys())