T = int(input())

for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))

    if N==1:
        print(max(arr[0][0], arr[1][0]))
    else:
        # dp[i][j]: [i][j]번째 뜯었을 때 얻는 최댓값
        dp = [[0]*N for _ in range(2)]
        dp[0][0], dp[1][0] = arr[0][0], arr[1][0]

        dp[0][1] = dp[1][0] + arr[0][1]
        dp[1][1] = dp[0][0] + arr[1][1]

        for i in range(2,N):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2], dp[0][i-2]) + arr[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2], dp[1][i-2]) + arr[1][i]

        print(max(max(dp[0]), max(dp[1])))