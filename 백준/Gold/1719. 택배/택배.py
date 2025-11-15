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
dist = [[INF]*(n+1) for _ in range(n+1)]    
answer = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dist[i][i] = 0
    for v,w in graph[i]:
        dist[i][v] = w

    for j in range(1,n+1):
        answer[i][j] = j


# 플로이드워셜
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            new_cost = dist[i][k] + dist[k][j]
            if new_cost < dist[i][j]:
                dist[i][j] = new_cost
                answer[i][j] = answer[i][k]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print('-', end=' ')
        else:
            print(answer[i][j], end=' ')
    print()
