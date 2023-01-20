M=0; row=0; col=0;
arr = [[0]*9 for i in range(9)]
for i in range(9):
    arr[i]=list(map(int, input().split()))
    for j in range(len(arr[i])):
        x=arr[i][j]
        if x>M:
            M=x; row=i; col=j
print(f'{M}\n{row+1} {col+1}')