N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[0])

# dp[i][j]: i번째 전깃줄 고려할 때, 전봇대 A 위치 j에서 가는 전깃줄 B의 위치
dp = [[0]*501 for _ in range(N)]
ends = [0]*501
for s,e in arr:
    ends[s] = e

for i in range(N):
    s,e = arr[i]
    temp = []
    for j in range(1,s+1):
        if j<s:
            dp[i][j] = dp[i-1][j]
            if ends[j]!=0 and ends[j] < e:
                temp.append(j)
        else:
            max_v = 0
            if temp:
                for k in temp:
                    max_v = max(max_v, dp[i-1][k])
            dp[i][j] = max(dp[i][j], max_v + 1)

print(N-max(dp[-1]))