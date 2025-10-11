def solution(alp, cop, problems):
    answer = 0
    a_max, c_max = alp, cop
    for a_req, c_req, _, _, _ in problems:
        a_max = max(a_req, a_max)
        c_max = max(c_req, c_max)
    # dp[a][c] = 알고력 값이 a이고 코딩력 값이 c일 때 최소 소요시간
    dp=[[1e9]*(c_max+1) for _ in range(a_max+1)]
    # 초기값
    dp[alp][cop] = 0
    for i in range(alp, a_max+1):
        for j in range(cop, c_max+1):
            if i+1<=a_max:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j+1<=c_max:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for a_req, c_req, a_rwd, c_rwd, cost in problems:
                if i>=a_req and j>=c_req:
                    ni = min(a_max, i+a_rwd)
                    nj = min(c_max, j+c_rwd)
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j]+cost)
    
    return dp[a_max][c_max]