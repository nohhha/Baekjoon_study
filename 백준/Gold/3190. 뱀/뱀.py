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
apples = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(K)]

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
    total_time += 1

    # 종료 조건
    if next_head[0]==-1 or next_head[0]==N or next_head[1]==-1 or next_head[1]==N:
        break
    if next_head in snake:
        break

    # 사과 여부
    snake.append(next_head)
    found = False
    for i in range(len(apples)):
        if next_head==apples[i]:
            apples.pop(i)
            found = True
            break
    if not found:
        snake.popleft()

    # 방향 전환
    if turns and total_time==turns[0][0]:
        _, degree = turns.popleft()
        dr = (dr + degree) % 4

print(total_time)