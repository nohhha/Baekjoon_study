import sys
import heapq
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

INF = 1e9
# 다익스트라
answer = []

def dijkstra(start):
    dist = [INF]*(n+1)
    next = [i for i in range(n+1)]
    q = []
    dist[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        cur_d, cur_v = heapq.heappop(q)
        if cur_d > dist[cur_v]:
            continue
        for new_v, new_d in graph[cur_v]:
            cost = cur_d + new_d
            if cost < dist[new_v]:
                dist[new_v] = cost
                heapq.heappush(q, (cost, new_v))
                if cur_v!=start:
                    next[new_v] = next[cur_v]

    return next

for i in range(1,n+1):
    next = dijkstra(i)

    for j in range(1,n+1):
        if i==j:
            print('-', end=' ')
        else:
            print(next[j], end=' ')
    print()
