nlist=list(input())
arr=[]
for n in nlist:
    arr.append(int(n))
arr.sort(reverse=True)
for n in arr:
    print(n, end="")
    