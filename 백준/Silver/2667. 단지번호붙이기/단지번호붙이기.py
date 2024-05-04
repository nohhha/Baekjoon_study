import sys
from collections import deque

n = int(input())
houses=[]
for _ in range(n):
    houses.append(list(map(int, input())))
    #1이 집이 있고, 0이 집이 없다

visited=[[False for _ in range(n)] for _ in range(n)]

def can_go(x, y):
    if not (x>=0 and x<n and y>=0 and y<n):
        return False
  
    if visited[x][y] or houses[x][y]==0:
        return False
  
    return True

def bfs():
    cnt=0
    dxs=[-1, 1, 0, 0]
    dys=[0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        cnt+=1

        for dx, dy in zip(dxs, dys):
            if can_go(x+dx, y+dy):
                visited[x+dx][y+dy]=True
                q.append((x+dx, y+dy))
  
    return cnt


house_count=[]
for i in range(n):
    for j in range(n):
        #시작점을 찾기
        if houses[i][j]==1 and not visited[i][j]:
            q=deque()
            q.append((i, j))
            visited[i][j]=True
            house_count.append(bfs())

print(len(house_count))
house_count.sort(reverse=False)
for i in range(len(house_count)):
    print(house_count[i])
