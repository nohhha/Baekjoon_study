N = int(input())
dp = [0]*N

dp[0] = 1
if N>=2:
    dp[1] = 3
if N>=3:
    for i in range(2, N):
        dp[i] = (dp[i-1] + dp[i-2]*2) % 10007

print(dp[-1])