import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def dfs(i,j):
    if dp[i][j]:
        return dp[i][j]

    dp[i][j] = 1
    for di,dj in dirs:
        ni,nj = i+di, j+dj
        if not (0<=ni<N and 0<=nj<N):
            continue
        if arr[i][j] < arr[ni][nj]:
            dp[i][j] = max(dp[i][j], dfs(ni,nj)+1)

    return dp[i][j]

dp = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not dp[i][j]:
            dfs(i,j)

print(max(map(max, dp)))