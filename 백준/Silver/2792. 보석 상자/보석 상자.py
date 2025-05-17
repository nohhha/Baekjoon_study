import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(M):
    arr.append(int(input()))

left = 1
right = max(arr) # 한 사람이 가질 수 있는 최대 보석 개수

ans = 0
while left<=right:
    mid = (left+right)//2
    total = 0
    for i in range(M):
        total += arr[i]//mid
        if arr[i]%mid!=0:
            total += 1
    # total이 N명 넘으면 안 돼, left 늘리기
    if total>N:
        left = mid+1
    # total<=N이면 기존 최소 질투심과 이번 질투심 비교해주고, right 줄여서 더 작은 질투심으로 탐색
    else:
        ans = mid
        right = mid-1
print(ans)
