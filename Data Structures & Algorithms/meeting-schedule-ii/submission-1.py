"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #create a start and end time of arrays
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        p1,p2=0,0
        count=0
        maxCount=0

        while p2<len(end) and p1<len(end):
            if start[p1]<end[p2]:
                count+=1
                p1+=1
            else:
                count-=1
                p2+=1
            maxCount=max(count, maxCount)
        return maxCount
           
