n=int(input())
nlist=list(map(int, input().split()))
nonprime=0
for i in range(n):
    num=nlist[i]
    if num==1:
        nonprime+=1
        continue
    for j in range(2, int(num**(1/2))+1):
        if num%j==0:
            nonprime+=1
            break
print(n-nonprime)