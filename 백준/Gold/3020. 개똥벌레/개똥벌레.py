import sys
input = sys.stdin.readline

N,H = map(int, input().split())
bottom, top = [0]*(H+1), [0]*(H+1)
start, end = 0,0
for i in range(N):
    h = int(input())
    if i%2==0:
        bottom[h] += 1
    else:
        top[h] += 1

bottom_sum, top_sum = [0]*(H+2), [0]*(H+2)
for t in range(H,0,-1):
    bottom_sum[t] = bottom_sum[t+1]+bottom[t]
    top_sum[t] = top_sum[t+1]+top[t]

answer = N+1
cnt = 0

for k in range(1,H+1):
    hit = bottom_sum[k] + top_sum[H-k+1]
    if hit < answer:
        answer = hit
        cnt = 1
    elif hit == answer:
        cnt += 1

print(answer, cnt)