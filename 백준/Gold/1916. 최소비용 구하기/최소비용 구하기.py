import sys
import heapq
input = sys.stdin.readline

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s,e,w = map(int, input().split())
    graph[s].append((e,w))
start, end = map(int, input().split())

INF = 1e9
dist = [INF]*(N+1)
q = []

# 시작 지점 초기화
dist[start] = 0
heapq.heappush(q, (0, start)) # 거리, 도시 번호

while q:
    cur_d, cur_v = heapq.heappop(q) # cur_v번 도시까지의 최소 거리 cur_d
    if dist[cur_v] < cur_d:
        continue

    for new_v, new_d in graph[cur_v]:
        cost = cur_d + new_d
        if cost < dist[new_v]:
            dist[new_v] = cost
            heapq.heappush(q, (cost, new_v))

print(dist[end])