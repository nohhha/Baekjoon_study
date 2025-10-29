from collections import deque

M,N = map(int, input().split())
arr = []
q = deque()
v = [[0]*M for _ in range(N)]
total = 0

for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):    
        if arr[i][j]==-1:
            v[i][j]=-1
        else:
            total += 1
            if arr[i][j]==1:
                q.append((i,j))
                v[i][j]=1

dxs = [-1,1,0,0]
dys = [0,0,-1,1]    

max_day = 0
cnt = len(q)
while q:
    ci,cj = q.popleft()
    for di,dj in zip(dxs, dys):
        ni,nj = ci+di,cj+dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0 and v[ni][nj]==0:
            q.append((ni,nj))
            v[ni][nj] = v[ci][cj]+1
            max_day = v[ni][nj]
            cnt += 1

if cnt<total:
    print(-1)
else:
    print(max(0, max_day-1))