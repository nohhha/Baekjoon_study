x=int(input())
arr=[[0]*100 for i in range(100)]
s=0
for i in range(x):
    a,b=map(int, input().split())
    for n in range(a, a+10):
        for m in range(b, b+10):
            if arr[n][m]==0:
                arr[n][m]=1
                s+=1
print(s)