import sys
import heapq
input = sys.stdin.readline

INF = 1e9
N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

# 2. X번 마을에서 모든 마을까지의 최소 거리
dist2 = [INF]*(N+1)
q = []

dist2[X] = 0
heapq.heappush(q, (0,X)) # 거리, 마을 번호

while q:
    cur_d, cur_v = heapq.heappop(q)
    if dist2[cur_v] < cur_d:
        continue

    for new_v, new_d in graph[cur_v]:
        cost = cur_d + new_d
        if cost < dist2[new_v]:
            dist2[new_v] = cost
            heapq.heappush(q, (cost, new_v))

max_dist = 0
# 시작 마을: i번 마을
for i in range(1, N+1):
    # 1. i번 마을에서 X번 마을까지 최소 거리
    dist = [INF]*(N+1)
    q = []

    dist[i] = 0
    heapq.heappush(q, (0,i)) # 거리, 마을 번호

    while q:
        cur_d, cur_v = heapq.heappop(q)
        if dist[cur_v] < cur_d:
            continue

        for new_v, new_d in graph[cur_v]:
            cost = cur_d + new_d
            if cost < dist[new_v]:
                dist[new_v] = cost
                heapq.heappush(q, (cost, new_v))

    max_dist = max(max_dist, dist[X]+dist2[i])

print(max_dist)