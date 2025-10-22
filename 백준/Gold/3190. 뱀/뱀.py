import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
snake = deque([(0,0)])
snake_size = 1
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
dr = 0

# 사과 개수
K = int(input())
apple_arr = [[0]*N for _ in range(N)]
for _ in range(K):
    i,j = map(lambda x: int(x)-1, input().split())
    apple_arr[i][j]=1

# 뱀의 방향 변환 횟수
L = int(input())
turns = deque()
for _ in range(L):
    t, degree = input().split()
    if degree == 'L':
        turns.append((int(t),-1))
    else:
        turns.append((int(t),1))

total_time = 0
while True:
    tail, head = snake[0], snake[-1]
    next_head = (head[0]+dirs[dr][0], head[1]+dirs[dr][1])
    nhi,nhj = next_head
    total_time += 1

    # 종료 조건
    if nhi==-1 or nhi==N or nhj==-1 or nhj==N:
        break
    if next_head in snake:
        break

    # 사과 여부
    snake.append(next_head)
    if apple_arr[nhi][nhj]==1:
        apple_arr[nhi][nhj]=0
    else:
        snake.popleft()

    # 방향 전환
    if turns and total_time==turns[0][0]:
        _, degree = turns.popleft()
        dr = (dr + degree) % 4

print(total_time)