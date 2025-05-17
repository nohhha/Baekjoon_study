
from collections import deque

N,K = map(int, input().split())


def bfs():
    v = [0 for _ in range(200000)]
    q = deque()
    v[N] = 1
    q.append(N)
    min_time = 200000
    cnt = 1
    while q:
        ci = q.popleft()
        if v[ci]>min_time:
            break
        if ci==K:
            if v[ci]<min_time:
                min_time=v[ci]
                cnt = 1
            elif v[ci]==min_time:
                cnt+=1
            continue

        for ni in [ci-1,ci+1,2*ci]:
            if 0<=ni<200000 and (v[ni]==0 or v[ni]==v[ci]+1):
                v[ni] = v[ci]+1
                q.append(ni)

    return min_time-1, cnt

time, cnt = bfs()
print(time)
print(cnt)