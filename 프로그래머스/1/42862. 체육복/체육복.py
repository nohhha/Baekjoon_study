def solution(n, lost, reserve):
    answer = 0
    
    # 여벌 체육복 가져온 학생이 도난당한 학생이기도 한 경우
    l_set, r_set = set(lost), set(reserve)
    dup = l_set & r_set
    l_set -= dup
    r_set -= dup
    
    for r in sorted(r_set):
        for l in sorted(l_set):
            if abs(l-r)==1:
                l_set.remove(l)
                break

    answer = n - len(l_set)
    return answer