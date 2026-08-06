class Solution:
    def jump(self, nums: List[int]) -> int:
        # this is like BFS because it checks first the window 
        # you can jump the furthest and then makes a decision
        # on what your next window should be

        #Greedy because we will choose the hifhest value 
        #each time

        totJump=0
        r,l=0,0 # window size
        while(r<len(nums)-1):
            furthest=0
            for i in range(l,r+1):
                furthest=max(furthest, nums[i]+i)
            #shifting window
            l=r+1
            r=furthest
            totJump+=1
        return totJump