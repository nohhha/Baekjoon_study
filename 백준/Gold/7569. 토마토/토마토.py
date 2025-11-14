import sys
from collections import deque
input = sys.stdin.readline

M,N,H = map(int, input().split())

arr = [[[] for _ in range(N)] for _ in range(H)]
q = deque()
v = [[[0]*M for _ in range(N)] for _ in range(H)]
total = 0
cnt = 0

for h in range(H):
    for i in range(N):
        arr[h][i] = list(map(int, input().split()))
        for j in range(M):
            if arr[h][i][j]!=-1:
                total += 1
            if arr[h][i][j]==1:
                q.append((h,i,j))
                v[h][i][j] = 1
                cnt += 1

moves = [(-1,0,0),(1,0,0),(0,0,-1),(0,0,1),(0,-1,0),(0,1,0)]
max_day = 0
while q:
    ch,ci,cj = q.popleft()
    for dh,di,dj in moves:
        nh,ni,nj = ch+dh, ci+di, cj+dj
        if 0<=nh<H and 0<=ni<N and 0<=nj<M and not v[nh][ni][nj] and arr[nh][ni][nj]==0:
            q.append((nh,ni,nj))
            v[nh][ni][nj] = v[ch][ci][cj] + 1
            cnt += 1
            max_day = max(max_day, v[nh][ni][nj])

if cnt==total:
    print(max(0,max_day-1))
else:
    print(-1)