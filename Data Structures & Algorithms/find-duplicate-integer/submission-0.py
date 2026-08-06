
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict1= {}
        for i, num in enumerate(nums):
            if num not in dict1:
                dict1[num]=[i]
            else:
                dict1[num].append(i)

        bestKey=None
        maxEl=-1
        for key,value in dict1.items():
            print(key, value)
            if len(value) > maxEl:
                bestKey=key
                maxEl=len(value)
        return bestKey