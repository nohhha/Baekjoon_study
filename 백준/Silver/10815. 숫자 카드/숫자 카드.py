N = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
M = int(input())
arr2 = list(map(int, input().split()))

def binary_search(start, end, num):
    while start<=end:
        mid=(start+end)//2
        # print(f'start:{start}, end:{end}, mid:{mid}')
        if arr1[mid]==num:
            return True
        elif arr1[mid]<num:
            start = mid+1
        else:
            end = mid-1
    return False

# 이분탐색 기준은 인덱스 !!!
start, end = 0, N-1
for num in arr2:
    if binary_search(start, end, num):
        print('1', end=' ')
    else:
        print('0', end=' ')