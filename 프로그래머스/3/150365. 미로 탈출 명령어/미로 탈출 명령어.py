def solution(n, m, x, y, r, c, k):
    answer = ''
    # 사전순이면 dlru 아래왼오른위 순서
    # 일단 s에서 e로 가까워지게 해서 도착
    # 도착한 후에 움직인 거리가 k미만이라면 dduu 하거나 llrr이런식으로 거리 늘리기
    x,y,r,c = x-1,y-1,r-1,c-1
    dirs = [('d',1,0),('l',0,-1),('r',0,1),('u',-1,0)]
    
    dist = abs(x-r)+abs(y-c)
    if dist > k or (dist%2)!=(k%2):
        return 'impossible'
    
    ci,cj = x,y
    while True:
        # 출구도착
        if (ci,cj)==(r,c) and len(answer)==k:          # 정답 일치
            return answer
                   
        for dr,di,dj in dirs:
            ni,nj = ci+di, cj+dj
            # 범위안 => 우선순위 있으니까 하나 되면 바로 break
            if 0<=ni<n and 0<=nj<m:
                # (ni,nj)로부터 (r,c)까지 남은 횟수 안에 도달 가능이어야 움직이기 가능
                if abs(ni-r)+abs(nj-c) <= k-(len(answer)+1):
                    ci,cj = ni,nj
                    answer += dr
                    break
    
    return answer