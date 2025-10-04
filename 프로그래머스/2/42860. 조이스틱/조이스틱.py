def solution(name):
    answer = 0
    N = len(name)

    for letter in name:
        min_cnt = min(ord(letter)-ord("A"), 1+ord("Z")-ord(letter))
        answer += min_cnt
    
    # 좌우 이동을 최소화
    move = N-1
    for i in range(N):
        j = i+1
        # i 다음부터 연속된 'A' 덩어리 끝(j) 찾기
        while j<N and name[j]=='A':
            j+=1
        # 오른쪽으로 갔다가 되돌아가서 끝 처리
        move = min(move, 2*i + (N-j))
        # 끝쪽 먼저 갔다가 되돌아와서 i 처리
        move = min(move, 2*(N-j) + i)
    
    answer += move
    
    return answer