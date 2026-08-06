class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for i in range(len(strs)):
            encoded+=(str(len(strs[i]))+"#"+strs[i])
            print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        output=[]
        i=0
        #i-> start
        #j-> end
        while(i<len(s)):
            j=i
            while (s[j]!='#'):
                j+=1
            lenStr= int(s[i:j])
            i=j+1
            j=j+1+lenStr
            output.append(s[i:j])
            i=j
            
        return output

            
            
            

