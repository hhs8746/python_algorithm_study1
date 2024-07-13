from collections import deque


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        num_island = 0
        #가로 세로
        n=len(grid[0])
        m= len(grid)
        visited=[[False]*n for _ in range(m)]

        def bfs(x,y):
            #x가 세로 y가 가로일때 x 연결되려면 아래와 같은 조합이면 가능(위아래로 한조합_)
            #만약 대각선도 연결되었다면 가능한 조합만 dx,dy에 추가하면 된다!
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            visited[x][y]=True
            queue = deque()
            queue.append((x,y))
            while queue:
                cur_x,cur_y = queue.popleft()
                for i in range(len(dx)):
                    next_x = cur_x +dx[i]
                    next_y = cur_y +dy[i]
                    if next_x>=0 and next_x <m and next_y >=0 and next_y <n:
                        if not visited[next_x][next_y] and grid[next_x][next_y] == "1":
                            visited[next_x][next_y] = True
                            queue.append((next_x,next_y))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i,j)
                    num_island+=1

    
        return num_island
