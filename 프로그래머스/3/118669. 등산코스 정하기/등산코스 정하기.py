import heapq

def solution(n, paths, gates, summits):
    INF = 1e9
    
    answer = []
    graph =[[] for _ in range(n+1)]
    for i, j, w in paths:
        graph[i].append([j,w])
        graph[j].append([i,w])
    
    is_summit = [False]*(n+1)
    for s in summits:
        is_summit[s] = True
    
    # dist[i]: i번 노드까지의 최소 intensity 저장
    dist = [INF]*(n+1)
    q = []
    for g in gates:
        dist[g] = 0
        heapq.heappush(q, [0, g])
    
    while q:
        d,i = heapq.heappop(q)
        if dist[i]<d or is_summit[i]:
            continue
        for j,dd in graph[i]:
            dd = max(dist[i], dd)
            if dist[j] > dd:
                dist[j] = dd
                heapq.heappush(q, [dd,j])
    
    result = [-1, INF]
    for s in sorted(summits):
        if dist[s] < result[1]:
            result = [s, dist[s]]
    return result
    
    
    return answer