n=int(input())
nlist=[]
rank=[1]*n
for i in range(n):
    x=tuple(map(int, input().split()))
    nlist.append(x)
    
for i in range(0, n-1):
    for j in range(i+1, n):
        if (nlist[i][0]>nlist[j][0]) & (nlist[i][1]>nlist[j][1]):
            rank[j]+=1
        elif (nlist[i][0]<nlist[j][0]) & (nlist[i][1]<nlist[j][1]):
            rank[i]+=1   

for i in range(n):
    print(rank[i], end=" ")