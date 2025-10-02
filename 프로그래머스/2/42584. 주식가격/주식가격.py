def solution(prices):
    N = len(prices)
    stack = []
    answer = [0]*N
    
    for i in range(N):
        while stack!=[] and stack[-1][1]>prices[i]:
            past, _ = stack.pop()
            answer[past] = i-past
        stack.append([i,prices[i]])
    
    for i,_ in stack:
        answer[i] = N-1-i
    
    return answer