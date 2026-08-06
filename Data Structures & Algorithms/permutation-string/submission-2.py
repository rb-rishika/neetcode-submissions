class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countsS2=[0]*26
        countsS1=[0]*26
        matches=0
        if len(s1)> len(s2):
            return False
        
        
        for i in range(len(s1)):
            countsS1[ord(s1[i])- ord('a')]+=1
            countsS2[ord(s2[i])- ord('a')]+=1

        if countsS1 == countsS2:
            return True

        for i in range(len(s1),len(s2)):
            countsS2[ord(s2[i])-ord('a')]+=1
            countsS2[ord(s2[i-len(s1)])-ord('a')]-=1
            if countsS1==countsS2:
                return True
        return False

            

        