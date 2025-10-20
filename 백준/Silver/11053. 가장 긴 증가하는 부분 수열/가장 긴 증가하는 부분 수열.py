N = int(input())
arr = list(map(int, input().split()))
# dp[i]: arr[i]를 마지막 값인 가장 긴 증가부분수열의 길이
dp = [1]*N

for i in range(1,N):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))