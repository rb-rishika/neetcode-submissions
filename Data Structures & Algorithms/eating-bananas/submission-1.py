class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r=1, max(piles)
        res=0
        while(l<=r):
            mid=l+(r-l)//2
            tot_time=0
            for i in piles:
                tot_time+=math.ceil(float(i)/mid)
            if tot_time<=h:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
                
        