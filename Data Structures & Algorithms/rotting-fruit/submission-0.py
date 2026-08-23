class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #we need a deque and BFS because we need to start from both sides.

        Q= deque()
        time=0
        fresh=0 # we need tos tore the count of fresh oranges
        ROWS, COLS= len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    Q.append([r,c])
                if grid[r][c]==1:
                    fresh+=1

        directions=[[-1,0],[1,0],[0,1],[0,-1]]

        while Q and fresh>0:
            for i in range(len(Q)): #this is the backbone of multisource BFS
                r,c=  Q.popleft()
                for dr, dc in directions:
                    if r+dr< 0 or r+dr >= ROWS or c+dc<0 or c+dc>=COLS or grid[r+dr][c+dc]!=1:
                        continue
                    grid[r+dr][c+dc]=2
                    Q.append([r+dr,c+dc])
                    fresh-=1
            time+=1 #at the end of the loop we would know how many oranges rotted in a sec
        return time if fresh== 0 else -1

