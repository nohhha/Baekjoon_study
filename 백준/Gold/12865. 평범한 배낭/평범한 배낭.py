N, K = map(int, input().split())

# dp[i][w]
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = map(int, input().split())
    for j in range(1, K+1):
        # i번째 무게가 j보다 크다면 넣을 수 없다 => dp[i-1][j]를 가져오기
        if j < w:
            dp[i][j] = dp[i-1][j]
        # (i-1번째 짐까지 + i번째 짐 넣었을 때)의 무게=j, dp[i-1][j]의 무게 비교
        else:
            dp[i][j] = max(v+dp[i-1][j-w], dp[i-1][j])

print(dp[N][K])