class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        diff= [0]*len(temperatures)

        #Brute force: 
        # for i in range(len(temperatures)-1):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j]> temperatures[i]:
        #             diff[i]=j-i
        #             break
        # return diff

        stack=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res
        

            



        