N,M = map(int, input().split())
ci,cj,dr = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

def can_clean_four_dirs(ci,cj):
    for di,dj in dirs:
        ni,nj = ci+di,cj+dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]+clean_arr[ni][nj]==0:
            return True
    return False

clean_arr = [[0]*M for _ in range(N)]
cnt = 0
while True:
    if clean_arr[ci][cj]==0:
        clean_arr[ci][cj]=1
        cnt += 1
    if not can_clean_four_dirs(ci,cj):
        # 한 칸 후진
        ni,nj = ci-dirs[dr][0], cj-dirs[dr][1]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
            ci,cj = ni,nj
            continue
        else:
            break
    else:
        dr = (dr-1)%4
        ni,nj = ci+dirs[dr][0], cj+dirs[dr][1]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]+clean_arr[ni][nj]==0:
            ci,cj = ni,nj

print(cnt)