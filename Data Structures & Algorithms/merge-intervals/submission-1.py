class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda val:val[0])
        #sorting it by first elem
        output=[intervals[0]]

        for start,end in intervals:
            last_index=output[-1][1]
            if start <= last_index:
                output[-1][1]= max(last_index,end)
            else:
                output.append([start,end])
        return output

        