class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        res=[]
        maxHeight=0

        for i in range(len(heights)-1,-1,-1):
            if maxHeight<heights[i]:
                res.append(i)
                maxHeight=heights[i]
        return sorted(res)