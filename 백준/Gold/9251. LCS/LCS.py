arr1 = input()
arr2 = input()

# dp[i] = 최장 공통 부분 수열
dp = [[0]*(len(arr2)+1) for _ in range(len(arr1)+1)]

for i in range(1, len(arr1)+1):
    for j in range(1, len(arr2)+1):
        if arr2[j-1] == arr1[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])