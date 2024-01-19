import heapq

def solution(operations):
    answer = []
    heap = []
    
    for o in operations:
        if o[0]=='I':
            heapq.heappush(heap, int(o[2:]))
        elif len(heap)>0:
            if o=='D 1':
                heap.pop()
            else:
                heapq.heappop(heap)

    if len(heap)==0:
        answer=[0,0]
    else:
        answer=[max(heap), min(heap)]
        
    return answer