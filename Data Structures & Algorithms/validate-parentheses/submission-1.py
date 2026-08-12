class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping_dict={'[':']', '(':')', '{':'}'}

        for char in s:
            if char in mapping_dict.keys():
                stack.append(char)
            elif stack and stack[-1]==list(mapping_dict.keys())[list(mapping_dict.values()).index(char)]:
                stack.pop()
            else:
                return False
        if stack: return False
        else: return True
        