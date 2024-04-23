n = int(input())

dp = [-1 for _ in range(n+1)]
dp[1]=0

for i in range(2, n+1):
    a=dp[int(i/3)]
    b=dp[int(i/2)]
    c=dp[i-1]
    if i%3==0 and i%2==0:
        dp[i] = min(a, min(b, c))+1
    elif i%3==0:
        dp[i] = min(a, c) + 1
    elif i%2==0:
        dp[i] = min(b, c) + 1
    else: #3, 2 둘 다 안 나누어 떨어질 때
        dp[i] = c + 1
    #print(f'dp{i}={dp[i]}')

print(dp[n])