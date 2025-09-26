def solution(m, n, puddles):
    answer = 0
    MAX = 201
    
    # 물웅덩이 좌표 배열에 맞게
    puds = {(y-1, x-1) for (x, y) in puddles}
    
    # 경로의 수 arr
    dp = [[0]*m for _ in range(n)]
    
    # 첫 행
    for i in range(n):
        if (i,0) in puds:
            for r in range(i,n):
                dp[r][0] = -1
            break
        dp[i][0] = 1
    # 첫 열
    for j in range(m):
        if (0,j) in puds:
            dp[0][j:] = [-1]*(m-j)
            break
        dp[0][j] = 1
    
    
    # 최단경로 개수 구하는 점화식 계산
    for i in range(1,n):
        for j in range(1,m):
            if (i,j) in puds:
                dp[i][j]=-1
            else:
                if dp[i-1][j]==-1:
                    dp[i][j] = dp[i][j-1]
                elif dp[i][j-1]==-1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
                
    if dp[n-1][m-1]==-1:
        answer = 0
    else:
        answer = dp[n-1][m-1]
        
    return answer