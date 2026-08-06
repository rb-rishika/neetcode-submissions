
class Solution:
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 
        visited=set()
        rows= len(grid)
        cols= len(grid[0])
        islands=0

        def BFS(row, col):
            queue=collections.deque()
            visited.add((row, col))
            queue.append((row, col))
            directions=[[-1,0],[0,-1],[1,0],[0,1]]

            while(queue):
                r,c= queue.popleft()
                for dr,dc in directions:
                    if ((0<=(r+dr)<rows) and (0<=(c+dc)<cols) and (grid[r+dr][c+dc]=="1") and ((r+dr, c+dc) not in visited )):
                        visited.add((r+dr, c+dc))
                        queue.append((r+dr, c+dc))
                    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1' and ((i,j)  not in visited):
                    BFS(i,j)
                    islands+=1
        return islands
                

    

        