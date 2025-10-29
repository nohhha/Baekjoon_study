from collections import deque

M,N = map(int, input().split())
arr = []
q = deque()
v = [[0]*M for _ in range(N)]

for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if arr[i][j]==1:
            q.append((i,j))
            v[i][j]=1
        elif arr[i][j]==-1:
            v[i][j]=-1

dxs = [-1,1,0,0]
dys = [0,0,-1,1]    

max_day = 0
while q:
    ci,cj = q.popleft()
    for di,dj in zip(dxs, dys):
        ni,nj = ci+di,cj+dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0 and v[ni][nj]==0:
            q.append((ni,nj))
            v[ni][nj] = v[ci][cj]+1
            max_day = v[ni][nj]

flag = True
for i in range(N):
    for j in range(M):
        if v[i][j]==0:
            flag=False
            break
    if not flag:
        break

if not flag:
    print(-1)
else:
    print(max(0, max_day-1))