N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[0])

# dp[i] = 최대증가수열
dp = [1]*N

for i in range(1,N):
    for j in range(0,i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))