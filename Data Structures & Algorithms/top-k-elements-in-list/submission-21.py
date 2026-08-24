from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
   
        
        
                #first we count the occurances
                #we will make a dictionary with frequesncies as key and the elements with that freq as value

        c1= Counter(nums)
        freqMap=[[] for i in range(len(nums)+1)]

    #     freqMap=[[],[],[]]
    #          0   1   2
        for key,value in c1.items():
            freqMap[value].append(key)

        res=[]

        for r in range(len(freqMap)-1,0,-1):
            res.extend(freqMap[r])
            if len(res)==k:
                return res
        
        return res[:k] 

        