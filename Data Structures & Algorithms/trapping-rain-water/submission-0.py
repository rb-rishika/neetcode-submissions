class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height)==0: return 0

        left= 0
        right= len(height)-1
        leftMax, rightMax= height[left], height[right]
        res=0

        # min(maxLeft, maxRight) - height[whichever index moved]

        while left<right:
            if leftMax< rightMax:
                left+=1
                leftMax=max(height[left], leftMax)
                res+=leftMax -height[left]

            else:
                right-=1
                rightMax=max(height[right], rightMax)
                res+=rightMax -height[right]
        return res
            
        