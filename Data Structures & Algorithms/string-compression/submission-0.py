class Solution:
    def compress(self, chars: List[str]) -> int:
        
        read,write=0,0

        while(read<len(chars)):
            chars[write]=chars[read]
            write+=1
            j=read+1

            while(j<len(chars) and chars[read]==chars[j]):
                j+=1 #count of a's
            
            if j-read> 1:
                for i in str(j-read):
                    chars[write]=i
                    write+=1
            read=j
        return write


        