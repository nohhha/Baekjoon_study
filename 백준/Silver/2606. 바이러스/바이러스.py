import sys
from collections import deque

n = int(input())
t = int(input())
connected = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(t):
    x, y = map(int, input().split())
    connected[x].append(y)
    connected[y].append(x)

def bfs():
    cnt=0

    while q:
        curr_v = q.popleft()

        for next_v in connected[curr_v]:
            if not visited[next_v]:
                cnt+=1
                visited[next_v]=True
                q.append(next_v)

    return cnt

q = deque()
q.append(1)
visited[1]=True
print(bfs())