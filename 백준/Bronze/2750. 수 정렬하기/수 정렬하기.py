n=int(input())
nlist=[]
for i in range(n):
  a=int(input())
  nlist.append(a)

sorted_nlist=sorted(nlist)

for i in range(len(sorted_nlist)):
  print(sorted_nlist[i])  