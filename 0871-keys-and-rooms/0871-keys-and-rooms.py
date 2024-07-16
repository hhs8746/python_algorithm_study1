from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #트리에서 BFS 시간 복잡도 O()
        visited = [False]*len(rooms)
        answer=[]

        def bfs(node):
            queue = deque()
            queue.append(node)
            visited[node] = True
            while queue:
                cur_v = queue.popleft()
                for next_v in rooms[cur_v]:
                    if not visited[next_v]:
                        visited[next_v]=True
                        queue.append(next_v)

        bfs(0)
        return all(visited)


        # def dfs(node):
        #     visited[node]=True
        #     for nb in rooms[node]:
        #         if not visited[nb]:
        #             dfs(nb)
        
        # for i in [0]: #range(len(rooms)):
        #     visited = [False]*len(rooms)
        #     ans = dfs(i)
        #     if False in visited:
        #         answer.append(False)
        #     else:
        #         answer.append(True)
        #     print(answer)
            
        # if True not in answer:
        #     return False
        # else:
        #     return True
