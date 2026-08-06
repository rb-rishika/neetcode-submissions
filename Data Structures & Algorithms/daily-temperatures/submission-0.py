class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps= temperatures
        answer=[0]*len(temps)
        stackTemps=[] # pair: [temp, index]

        for i, t in enumerate(temps):
            while stackTemps and t > stackTemps[-1][0]:
                stackT, stackInd = stackTemps.pop()
                answer[stackInd]=i-stackInd
            stackTemps.append([temps[i], i])
        return answer