import sys
input = sys.stdin.readline

R,C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]

dxs = [-1,1,0,0] # 상하좌우
dys = [0,0,-1,1]

global answer
answer = 0

def dfs(ci,cj,alp_bit,cnt):
    global answer
    answer = max(answer, cnt)

    for di,dj in zip(dxs, dys):
        ni,nj = ci+di, cj+dj
        if not (0<=ni<R and 0<=nj<C):
            continue

        next = arr[ni][nj]
        next_bit = 1<<(ord(next)-ord('A'))
        if next_bit & alp_bit:
            continue

        dfs(ni,nj, alp_bit|next_bit, cnt+1)

alp_bit = 1<<(ord(arr[0][0]) - ord('A'))
dfs(0,0,alp_bit,1)

print(answer)