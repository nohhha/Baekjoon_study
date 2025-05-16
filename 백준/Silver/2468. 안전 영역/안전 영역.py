import sys
sys.setrecursionlimit(100000)

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(height,ci,cj):
    for di,dj in zip(dx,dy):
        ni,nj = ci+di, cj+dj
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]>height and v[ni][nj]==0:
            v[ni][nj]=1
            dfs(height,ni,nj)

max_cnt = 1
for height in range(1, 101):
    v = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > height and v[i][j] == 0:
                v[i][j]=1
                dfs(height,i,j)
                cnt += 1
    max_cnt = max(max_cnt,cnt)

print(max_cnt)