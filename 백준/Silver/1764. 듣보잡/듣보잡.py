n,m=map(int, input().split())

N=set()
for i in range(n):
    N.add(input())
M=set()
for i in range(m):
    M.add(input())
    
result=sorted(list(N&M))
print(len(result))
for name in result:
    print(name)