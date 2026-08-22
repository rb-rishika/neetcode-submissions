class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i,currString):
            if len(currString)==len(digits):
                res.append(currString)
                return
            #i=0, digits[i]=3, "def"
            for c in digitToChar[digits[i]]:
                dfs(i+1, currString+c)
        if digits: 
            dfs(0,"")
        return res