n = int(input())

# dp[i] = ikg에 들어갈 최소 봉지 개수
dp=[-1 for _ in range(5001)]
dp[3]=1
dp[5]=1

for i in range(6, n+1):
    a=dp[i-5]
    b=dp[i-3]
    if a==-1 and b==-1:
        dp[i]==-1
    elif a==-1 or (b!=-1 and b<a):
        dp[i]=b+1
    elif b==-1 or (a!=-1 and a<=b):
        dp[i]=a+1

print(dp[n])