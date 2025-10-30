N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
alpha_lst = [0]*26
for i in range(N):
    for j in range(len(arr[i])):
        idx = ord(arr[i][j]) - ord("A")
        alpha_lst[idx] += 10**(len(arr[i])-1-j)

answer = 0
num = 9
for i in sorted(alpha_lst, reverse=True):
    if num==0 or i==0:
        break
    answer += i*num
    num -= 1

print(answer)