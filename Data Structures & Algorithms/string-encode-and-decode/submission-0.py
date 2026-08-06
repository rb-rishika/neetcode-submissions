class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for i in range(len(strs)):
            encoded+=(str(len(strs[i]))+"#"+strs[i])
            print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        op=[]
        i=0
        while(i<len(s)):
            j=i #i start of index #j-> ending index
            while(s[j]!="#"):
                j+=1
            lenStr= int(s[i:j])
            i=j+1 
            j=i+lenStr
            op.append(s[i:j])
            i=j
        return op
        

            
            
            

