N,M = map(int, input().split())
arr = list(map(int, input().split()))

# M개의 블루레이에 들어갈 크기 최솟값 찾기
start, end = max(arr), sum(arr)

while start <= end:
    mid = (start+end)//2

    total = 0
    cnt = 1
    for val in arr:
        if total + val > mid:
            cnt += 1
            total = 0
        total += val

    if cnt <= M:
        end = mid-1
        answer = mid
    else:
        start = mid+1

print(answer)