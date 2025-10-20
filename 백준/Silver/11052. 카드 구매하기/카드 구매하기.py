N = int(input())
arr = [0] + list(map(int, input().split()))

# dp[i][j] = 카드 i번째까지 고려했을 때 j개를 구매하기 위한 금액의 최댓값
dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    cost = arr[i]
    for j in range(1, N+1):
        if i>j:
            dp[i][j] = max(dp[i-1][j], dp[i][j])
        else:
            dp[i][j] = max(dp[i][j-i]+cost, dp[i-1][j], dp[i][j])

print(dp[-1][-1])