def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    for i in range(len(citations)):
        c = citations[i]
        if c < i+1:
            return i
        
    return len(citations)