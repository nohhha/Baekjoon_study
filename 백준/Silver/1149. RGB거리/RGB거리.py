N = int(input())
arr = [[]]
for _ in range(N):
    arr.append(list(map(int, input().split())))

# red[i] = i번째 집을 red로 칠하는 최소 비용
red, green, blue = [0]*(N+1), [0]*(N+1), [0]*(N+1)

for i in range(1, N+1):
    if i==1:
        red[i], green[i], blue[i] = arr[i]
    else:
        r,g,b = arr[i]
        red[i] = min(green[i-1], blue[i-1]) + r
        green[i] = min(blue[i-1], red[i-1]) + g
        blue[i] = min(red[i-1], green[i-1]) + b

print(min(red[N], green[N], blue[N]))