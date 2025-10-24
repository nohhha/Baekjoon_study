T = int(input())
for _ in range(T):
    N,M = map(int, input().split())
    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1,M+1):
        dp[1][i] = i

    for i in range(2,N+1):
        for j in range(2,M+1):
            dp[i][j] += sum(dp[i-1][i-1:j])

    print(dp[N][M])