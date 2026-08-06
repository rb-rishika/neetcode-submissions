class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        setNumber=set()
        for num in nums:
            if num in setNumber:
                setNumber.remove(num)
            else:
                setNumber.add(num)
            
        return setNumber.pop()
        