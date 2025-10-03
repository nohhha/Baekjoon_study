from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    max_count = len(q1) + len(q2) + 2
    
    if (sum1+sum2)%2!=0:
        return -1
    
    while sum1 != sum2:
        if answer<=max_count:
            if sum1 < sum2:
                n = q2.popleft()
                q1.append(n)
                sum1, sum2 = sum1+n, sum2-n
            else: # sum1 > sum2
                n = q1.popleft()
                q2.append(n)
                sum1, sum2 = sum1-n, sum2+n
            answer += 1
        else:
            return -1    
    
    return answer