T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0]*(N+1)
    
    # 초기화
    dp[1] = 1
    if N>=2:
        dp[2] = 2
    if N>=3:
        dp[3] = 4

    # 점화식
    if N>=4:
        for i in range(4, N+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    print(dp[N])