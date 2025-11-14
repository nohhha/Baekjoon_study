import sys
import heapq
input = sys.stdin.readline

V,E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

INF = 1e9
dist = [INF]*(V+1)
hq = []

# 시작 원소 초기화
dist[start] = 0
heapq.heappush(hq, (0,start)) # 거리, 노드번호

while hq:
    cur_d, cur_v = heapq.heappop(hq)
    if dist[cur_v] < cur_d:
        continue

    for new_v, new_d in graph[cur_v]:
        cost = cur_d + new_d
        # 더 짧은 경로를 찾은 노드 정보들은 우선순위 큐에 넣는다
        if cost < dist[new_v]:
            dist[new_v] = cost
            heapq.heappush(hq, (cost, new_v))


for i in range(1,V+1):
    if dist[i]==INF:
        print('INF')
    else:
        print(dist[i])