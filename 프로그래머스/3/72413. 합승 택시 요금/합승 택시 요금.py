import heapq
INF = 1e9

def dijkstra(n, graph, start):
    dist = [INF]*(n+1)
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        cur_d, cur_v = heapq.heappop(q)
        if dist[cur_v] < cur_d:
            continue
        for new_v, new_d in graph[cur_v]:
            cost = cur_d + new_d
            if cost < dist[new_v]:
                dist[new_v] = cost
                heapq.heappush(q, (cost, new_v))
    
    return dist

def solution(n, s, a, b, fares):
    answer = 0
    # 1. 각자 최저 요금 계산: s->a, s->b
    # 2. 중간 지점 k를 정해서 계산 s->k, k->b, k->a
    graph = [[] for _ in range(n+1)]
    for c,d,f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f))
    
    # 시작점: s
    dist_s = dijkstra(n, graph, s)
    answer = dist_s[a] + dist_s[b]
    
    # 시작점: 임의의 k
    for k in range(1,n+1):
        if k==s:
            continue
        dist_k = dijkstra(n, graph, k)
        answer = min(answer, dist_s[k] + dist_k[a] + dist_k[b])
    
    
    return answer