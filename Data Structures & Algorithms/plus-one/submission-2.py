class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in range(len(digits)-1, -1, -1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        
        return [1]+ digits #case [9,9,9]-> [1,0,0,0]