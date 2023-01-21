n=int(input())
nlist=[]
for i in range(10000000):
    if '666' in str(i):
        nlist.append(i)
        if len(nlist)==n:
            print(nlist[n-1])