from collections import deque

def solution(progresses, speeds):
    answer = []
    
    N = len(progresses)
    days = [0]*N
    for i in range(N):
        day = 0
        now = progresses[i]
        while now<100:
            now += speeds[i]
            day += 1
        days[i] = day
    
    for today in range(max(days)+1):
        cnt = 0
        while days and days[0]<=today:
            days.pop(0)
            cnt += 1
        if cnt>0:
            answer.append(cnt)
    
    return answer