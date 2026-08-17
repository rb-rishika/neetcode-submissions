class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack=[]
        maxArea=0

        for i,height in enumerate(heights):
            start=i
            #we will enter while loop if the height of the stack is more than that of the 
            while stack and stack[-1][1]> height:
                index, h= stack.pop()
                maxArea=max(maxArea, h* (i-index))
                start= index
            stack.append([start,height])

        #now, we resolve the remainders of the stack.. the smaller height elements,

        for i,height in (stack):
            maxArea= max(maxArea, height*(len(heights)-i))
        return maxArea
        