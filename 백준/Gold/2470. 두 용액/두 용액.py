N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left, right = 0, N-1

answer = abs(arr[0]+arr[-1])
answer_set = [arr[0],arr[-1]]

while left<right:
    a,b = arr[left], arr[right]
    if abs(a+b) < answer:
        answer = abs(a+b)
        answer_set = [a,b]
        if answer==0:
            break
    if a+b<0:
        left+=1
    else:
        right-=1

print(*answer_set)