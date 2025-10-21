N, K = map(int, input().split())

dp = [0]*(K+1)

for i in range(N):
    coin = int(input())
    for j in range(1,K+1):
        if j < coin:
            continue
        elif j == coin:
            dp[j] += 1
        else:
            dp[j] += dp[j-coin]
print(dp[-1])