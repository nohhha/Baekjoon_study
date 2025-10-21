import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# -1은 미방문
dp = [[-1]*M for _ in range(N)]
dirs = [(0,1),(0,-1),(1,0),(-1,0)]

def dfs(i,j):
    if i==N-1 and j==M-1:
        return 1
    if dp[i][j] == -1:
        dp[i][j] = 0
        for di,dj in dirs:
            ni,nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] < arr[i][j]:
                dp[i][j] += dfs(ni,nj)
    return dp[i][j]

print(dfs(0,0))