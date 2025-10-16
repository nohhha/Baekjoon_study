N = int(input())
dp = [0]*(N+1)

# 초기화
dp[1] = 1
if N>=2:
    dp[2] = 2

# 점화식
if N>=3:
    for i in range(3,N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[N])