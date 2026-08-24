class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]
        i=0
        dict_map={'[':']', '{':'}','(':')'}

        while(i<len(s)):
            if s[i] in dict_map.keys():
                stack.append(s[i])
            else: 
                if not stack or not dict_map[stack.pop()] == s[i] :
                    return False
            i+=1

        return True if len(stack)==0 else False
