def solution(numbers):
    answer = ''
    
    numbers.sort(key=lambda x: str(x)*3, reverse=True)
    answer = ''.join(map(str, numbers))
    if int(answer)==0:
        answer = "0"
    
    return answer