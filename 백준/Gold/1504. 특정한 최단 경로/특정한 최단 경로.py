import sys
import heapq
input = sys.stdin.readline

INF = 1e9
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    # a,b 정점 사이 양방향 거리 c
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, input().split())

# start -> v1 -> v2 -> end
# start -> v2 -> v1 -> end

dist = [[INF]*(N+1) for _ in range(3)]
for idx,start in enumerate([1, v1, v2]):
    q = []

    dist[idx][start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cur_d, cur_v = heapq.heappop(q)
        if dist[idx][cur_v] < cur_d:
            continue

        for new_v, new_d in graph[cur_v]:
            cost = cur_d + new_d
            if cost < dist[idx][new_v]:
                dist[idx][new_v] = cost
                heapq.heappush(q, (cost, new_v))

d1 = dist[0][v1] + dist[1][v2] + dist[2][N]
d2 = dist[0][v2] + dist[2][v1] + dist[1][N]
if d1>=INF and d2>=INF:
    print(-1)
else:
    print(min(d1,d2))