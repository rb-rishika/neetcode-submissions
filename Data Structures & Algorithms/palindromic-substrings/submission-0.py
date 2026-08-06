class Solution:
    def countSubstrings(self, s: str) -> int:
        # two situations: even and odd length
        # we start from middle and work till end 
        total=0

        for i in range(len(s)):
            #odd length 
            l,r=i,i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                total+=1
                l-=1
                r+=1
            
            #even len
            l,r=i,i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                total+=1
                l-=1
                r+=1
        return total