arr = list(map(int, input()))
N = len(arr)

if arr[0]==0:
    print(0)
else:
    arr = [0]+arr
    dp = [0]*(N+1)
    dp[0] = dp[1] = 1

    for i in range(2,N+1):
        if arr[i]==0:
            if arr[i-1]==1 or arr[i-1]==2:
                dp[i] = dp[i-2]
            else:       # 암호 잘못되어 해석할 수 없는 경우
                dp[-1] = 0
                break

        elif arr[i-1]==1 or (arr[i-1]==2 and arr[i]<=6):
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]

        dp[i] = dp[i]%1000000

    print(dp[N])