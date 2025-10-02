import heapq as hq

def solution(jobs):
    answer = 0
    # 우선순위: 작업의 소요시간 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것
    # jobs: [작업이 요청되는 시점, 작업의 소요시간]
    N = len(jobs)
    ready = []
    now = 0
    complete = 0
    
    while complete<N:
        
        for i in range(len(jobs)-1, -1, -1):
            job = jobs[i]
            # 요청시각이 현재보다 이전인 것들 ready 에 추가
            if job[0]<=now:
                # (소요시간, 요청시각)
                hq.heappush(ready, (job[1],job[0]))
                jobs.pop(i)
        
        # 대기 중인 작업 있으면
        if len(ready)>0:
            duration, start = hq.heappop(ready)
            now += duration
            complete += 1
            answer += (now-start)
        else:
            now += 1
    
    return answer//N