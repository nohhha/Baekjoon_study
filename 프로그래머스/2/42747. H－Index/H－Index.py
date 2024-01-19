def solution(citations):
    answer = 0
    citations.sort()
    for i, h in enumerate(citations):
        if h >= len(citations)-i:
            answer=len(citations)-i
            break
    return answer