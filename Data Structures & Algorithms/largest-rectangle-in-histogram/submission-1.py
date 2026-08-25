class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # stack=[]
        # maxArea=0

        # for i,height in enumerate(heights):
        #     start=i
        #     #we will enter while loop if the height of the stack is more than that of the 
        #     while stack and stack[-1][1]> height:
        #         index, h= stack.pop()
        #         maxArea=max(maxArea, h* (i-index))
        #         start= index
        #     stack.append([start,height])

        # #now, we resolve the remainders of the stack.. the smaller height elements,

        # for i,height in (stack):
        #     maxArea= max(maxArea, height*(len(heights)-i))
        # return maxArea


        stack=[]
        heights=heights+[0]
        maxArea=0

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]]> heights[i]:
                idx=stack.pop()
                height= heights[idx]
                width= i if not stack else i-stack[-1]-1
                maxArea= max(maxArea, height* width) 
            stack.append(i)
        return maxArea




# # Example
# heights = [2, 1, 5, 6, 2, 3]
# print(largest_rectangle_area(heights))  # Output: 10

        