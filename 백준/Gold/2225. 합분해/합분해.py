N, K = list(map(int, input().split()))
# dp[i][j] = j개의 숫자로 합이 i가 되도록 하는 경우의 수
dp = [[0]*(K+1) for _ in range(N+1)]
dp[0] = [1]*(K+1)
for i in range(1,N+1):
    for j in range(1,K+1):
        # dp[i][j] = dp[0][j-1] + dp[1][j-1] + ... + dp[i-1][j-1] + dp[i][j-1]
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(dp[-1][-1]%1000000000)