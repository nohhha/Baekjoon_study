

def add_cnt(alpha, i):
    lst = ["A", "E", "I", "O", "U"]
    cnt  = 1
    for j in range(1, 6-i):
        cnt += 5**j
    cnt *= lst.index(alpha)
    return cnt+1

def solution(word):
    answer = 0
    # "A"부터 "E"사이에는 1 + 5**1 + 5**2 + 5**3 + 5**4
    # "AA"부터 "AE" 사이에는 1 + 5**1 + 5**2 + 5**3
    
    # 알파벳과 자릿수를 받으면 ("I", "1") 시작 위치를 알려주기 =>  2*(5**1 + 5**2 + 5**3 + 5**4)
    for i,alpha in enumerate(word):
        answer += add_cnt(alpha, i+1)
        
    return answer