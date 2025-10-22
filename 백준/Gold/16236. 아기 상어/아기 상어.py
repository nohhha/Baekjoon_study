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

def find_closest_fish(si,sj):
    fish_lst = []
    for i in range(N):
        for j in range(N):
            if 0 < arr[i][j] < shark:
                dist = bfs(si,sj,i,j)
                if dist==-1:
                    continue
                fish_lst.append((dist, i, j))
    if not fish_lst:
        return (-1,-1,-1)
    fish_lst.sort(key=lambda x: (x[0],x[1],x[2]))
    return fish_lst[0]

def bfs(si,sj,ei,ej):
    # 상어로부터 거리가 물고기까지 지나가야하는 칸의 개수
    v = [[0]*N for _ in range(N)]
    q = deque()
    v[si][sj]=1
    q.append((si,sj))
    while q:
        ci,cj = q.popleft()
        if (ci,cj)==(ei,ej):
            return v[ci][cj]-1

        for di,dj in dirs:
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]<=shark:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj]+1
    return -1

cnt = 0
ans = 0
while cnt < total_cnt:
    dist,ni,nj = find_closest_fish(ci,cj)
    if (dist,ni,nj)==(-1,-1,-1):
        break
    arr[ni][nj] = 0
    cnt += 1
    ans += dist
    ci,cj = ni,nj
    if cnt==(shark*(shark+1)//2 - 1):
        shark += 1

print(ans)