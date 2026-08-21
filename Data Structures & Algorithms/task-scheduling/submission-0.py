from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # maxFreq
        # AAAABB n=2
        # A_ _A_ _A_ _A

        # AB _AB _A_ _A

        # {A:4, B:2}
        # idle= (4-1)*2=6
        # min(4-1,2)=2 , it will fill two gaps 6-2=4

        c1= dict(Counter(tasks))
        c2=sorted(c1.items(), key=lambda x:x[1], reverse=True)
        maxf = c2[0][1]
        
        empty_slots=(maxf-1)*n
        for key, value in (c2[1:]):
            empty_slots-= min(maxf-1,value)
        return max(empty_slots,0) + len(tasks)

        


