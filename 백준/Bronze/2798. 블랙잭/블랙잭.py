n,m=map(int, input().split())
nlist=list(map(int, input().split()))
dif=m
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            x=nlist[i]+nlist[j]+nlist[k]
            if (m-x<dif) & (m-x>=0):
                total=x
                dif=m-x
print(total)
                