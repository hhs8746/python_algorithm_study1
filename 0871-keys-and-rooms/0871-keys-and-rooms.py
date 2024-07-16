class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #트리에서 DFS 시간 복잡도 O(V+E(노드 + 엣지))
        visited = [False]*len(rooms)
        answer=[]
        def dfs(node):
            visited[node]=True
            for nb in rooms[node]:
                if not visited[nb]:
                    dfs(nb)
        
        for i in [0]: #range(len(rooms)):
            visited = [False]*len(rooms)
            ans = dfs(i)
            if False in visited:
                answer.append(False)
            else:
                answer.append(True)
            print(answer)
            
        if True not in answer:
            return False
        else:
            return True
