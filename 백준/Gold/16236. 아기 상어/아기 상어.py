import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
shark = 2
total_cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]==9:
            ci,cj = i,j
            arr[i][j]=0
        elif arr[i][j]!=0:
            total_cnt += 1

dirs = [(-1,0),(0,-1),(0,1),(1,0)]

def bfs(si,sj):
    # 상어가 갈 수 있는 물고기 거리,위치 리스트
    fish = []

    v = [[0]*N for _ in range(N)]
    q = deque()
    v[si][sj]=1
    q.append((si,sj))

    while q:
        ci,cj = q.popleft()
        for di,dj in dirs:
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
                if 0<=arr[ni][nj]<=shark:
                    q.append((ni,nj))
                    v[ni][nj] = v[ci][cj]+1
                    if 0<arr[ni][nj]<shark:
                        fish.append((v[ni][nj]-1,ni,nj))
    fish.sort(key=lambda x: (x[0],x[1],x[2]))
    return fish

cnt = 0
ans = 0
while cnt < total_cnt:
    fish_cand = bfs(ci,cj)
    if not fish_cand:
        break
    dist,ni,nj = fish_cand[0]
    arr[ni][nj] = 0
    cnt += 1
    ans += dist
    ci,cj = ni,nj
    if cnt==(shark*(shark+1)//2 - 1):
        shark += 1

print(ans)