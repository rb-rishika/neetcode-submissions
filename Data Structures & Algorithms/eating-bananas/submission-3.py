class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #brute force. We compute piles we are able to eat at max speed.
        # for k in range(1, max(piles) + 1):
        #     hours_needed=0
        #     for pile in piles:
        #         hours_needed+=((pile+k-1)//k)
        #     if hours_needed<=h:
        #         return k
        # return 0

        low=1
        high= max(piles)
        ans=max(piles)

        while low<=high:
            mid = (low + high) // 2
            hours_needed=0
            for pile in piles:
                hours_needed += (pile + mid - 1) // mid
            if hours_needed<=h:
                ans= mid
                high=mid-1
            else:
                low=mid+1
        return ans



