arr = []
for i in range(9):
    arr.append((int(input())))
arr.sort()
total = sum(arr)

def find_num():
    for i in range(8): # 0~7
        for j in range(i+1, 9): # i+1~8
            if total-arr[i]-arr[j]==100:
                return i,j

i,j = find_num()
for k in range(len(arr)):
    if k!=i and k!=j:
        print(arr[k])
