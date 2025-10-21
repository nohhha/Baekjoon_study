N,K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

# dp[i] : 가치 합이 i가 되는 동전의 최소 개수
dp = [1e9]*(K+1)

# 동전 하나씩 돌면서
for i in range(N):
    cur = arr[i]
    # 가치 합이 j가 되는 최소 개수 갱신
    for j in range(1,K+1):
        if cur < j:
            dp[j] = min(dp[j-cur] + dp[cur], dp[j])
        elif cur == j:
            dp[j] = 1
        else:
            continue

if dp[-1]==1e9:
    print(-1)
else:
    print(dp[-1])