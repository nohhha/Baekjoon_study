n,m=map(int, input().split())
temp=[[0 for j in range(m)] for i in range(n)]
arr=[[0 for j in range(m)] for i in range(n)]

for x in range(2):
    for i in range(n):
        arr[i]=list(map(int, input().split()))
        for j in range(m):
            temp[i][j]+=arr[i][j]

for row in temp:
    for x in row:
        print(x, end=" ")
    print() 