import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)

    while len(heap)>=2:
        first = heapq.heappop(heap)
        if first>=K:
            break
        second = heapq.heappop(heap)
        new = first + 2*second
        heapq.heappush(heap, new)
        answer+=1
        
    if heap[0]<K:
        answer=-1
        
    return answer