def solution(triangle):
    answer = 0
    r = len(triangle)
    c = len(triangle[-1])
    
    dp = [[0]*c for _ in range(r)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j==0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    answer = max(dp[-1])
    
    return answer