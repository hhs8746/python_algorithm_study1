from collections import deque

class Solution:
    #최단경로, 미로찾기는 출발점 부터 가기 때문에 bfs가 유리하다!
    #dfs는 최단경로가 아닐수도 있으므로 모든 경우의 수를 다 보고 비교해야해서 비효율

    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        shortlength = -1
        row=len(grid)
        col=len(grid[0])
        if grid[0][0] ==1 or grid[row-1][col-1] ==1:
            return shortlength
            
        visited=[[False]*col for ll in range(row)]
        queue = deque()
        queue.append((0,0,1))
        visited[0][0]=True
        #동서남북 + 대각선
        delta = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        while queue:
            cur_r,cur_c,cur_len= queue.popleft()
            #목적지에 도착했을때 그때의 cur_len을 shortest_path_len에 저장하면 된다.
            if cur_r == row-1 and cur_c == col-1:
                shortlength = cur_len
                break
            visited[cur_r][cur_c]
            
            for dr,dc in delta:
                next_r = cur_r + dr
                next_c = cur_c + dc
                if next_r >=0 and next_r < row and next_c >=0 and next_c < col:
                    if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                        queue.append((next_r,next_c,cur_len+1))
                        visited[next_r][next_c] = True

        return shortlength