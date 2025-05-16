from collections import deque

N,M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

# 최소 칸의 수 => bfs
def bfs():
    q = deque()
    q.append((0,0))
    v = [[0 for _ in range(M)] for _ in range(N)]
    v[0][0] = 1

    while q:
        ci,cj = q.popleft()
        # 종료 조건: (N-1,M-1)에 도달
        if ci==N-1 and cj==M-1:
            return v[ci][cj]
        # 인접한 네 방향
        for di,dj in zip(dxs, dys):
            ni = ci+di
            nj = cj+dj
            # 범위 안, 이동가능칸(=1), 방문전(=0)
            if ni>=0 and ni<N and nj>=0 and nj<M and arr[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni, nj))
                v[ni][nj]=v[ci][cj]+1

ans = bfs()
print(ans)