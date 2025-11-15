from collections import deque
INF = 1e9

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    start = 1
    
    dist = [INF]*(n+1)
    q = deque()
    dist[start] = 0
    q.append(start)
    
    max_v = 0
    answer = 0
    while q:
        ci = q.popleft()
        for ni in graph[ci]:
            if dist[ni]!=INF:
                continue
            dist[ni] = dist[ci]+1
            q.append(ni)
            if dist[ni]==max_v:
                answer += 1
            elif dist[ni]>max_v:
                answer = 1
                max_v = dist[ni]
        
    return answer