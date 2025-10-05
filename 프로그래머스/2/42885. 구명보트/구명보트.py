def solution(people, limit):
    # 구명보트 개수의 최솟값    
    answer = 0
    people.sort()
    
    i, j = 0, len(people)-1
    while True:
        if i==j:
            answer += 1
            return answer
        if i>j:
            return answer

        if people[i]+people[j]<=limit:
            i, j = i+1, j-1
            answer += 1
        else:
            j -= 1
            answer += 1
    
    
    return answer