from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for i, p in enumerate(priorities):
        queue.append((i,p))
    
    while len(queue)>0:
        max_p = max([q[1] for q in queue])
        current = queue.popleft()
        if current[1]<max_p:
            queue.append(current)
        else:
            answer+=1
            if current[0]==location:
                return answer