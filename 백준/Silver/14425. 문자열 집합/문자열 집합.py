n,m=map(int, input().split())
S=[]
for i in range(n):
    S.append(input())
S=set(S)
cnt=0
for i in range(m):
    test=input()
    if test in S:
        cnt+=1
print(cnt)