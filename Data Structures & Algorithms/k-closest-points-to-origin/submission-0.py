class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #euclidean distance without sqrt
        distMapping=[[x*x+y*y, (x,y)] for x,y in points]
        distMapping.sort(key= lambda x: x[0])

        return [[x,y] for _,(x,y) in distMapping[:k]]
        