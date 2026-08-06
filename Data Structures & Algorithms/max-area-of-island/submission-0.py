from typing import List
import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 
        
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def BFS(row, col):
            queue = collections.deque()
            visited.add((row, col))
            queue.append((row, col))
            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            counter = 1

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        grid[nr][nc] == 1 and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        counter += 1

            return counter
        
        area = 0            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = max(area, BFS(i, j))
                    
        return area