import sys
input = sys.stdin.readline

n,m=map(int, input().split())
S=set()
for i in range(n):
    S.add(input())

cnt=0
for i in range(m):
    test=input()
    if test in S:
        cnt+=1
print(cnt)