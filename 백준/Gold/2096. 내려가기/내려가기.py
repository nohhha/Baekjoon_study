N = int(input())

# max_dp[i] = i번째 줄에서의 최대 점수 합
max0, max1, max2 = map(int, input().split())
min0, min1, min2 = max0, max1, max2

for i in range(1,N):
    n0,n1,n2 = map(int, input().split())
    nmax0 = max(max0,max1) + n0
    nmax1 = max(max0,max1,max2) + n1
    nmax2 = max(max1,max2) + n2
    max0, max1, max2 = nmax0, nmax1, nmax2

    nmin0 = min(min0,min1) + n0
    nmin1 = min(min0,min1,min2) + n1
    nmin2 = min(min1,min2) + n2
    min0, min1, min2 = nmin0, nmin1, nmin2

print(max(max0,max1,max2), min(min0,min1,min2))