def solution(friends, gifts):
    answer = 0
    
    # (A,B) 주고받은 기록 있고, 수가 달라
        # 적게 선물한 사람 -> 많이 선물한 사람
    # 주고받은 기록 x or 수가 같아
        # 선물 지수 작은 사람 -> 선물 지수 큰 사람
        # 선물 지수: 준 선물 수 - 받은 선물 수
        # 선물 지수도 같다면 주고받기x
    
    N = len(friends)
    arr = [[0]*N for _ in range(N)]
    arr2 = [[0]*3 for _ in range(N)]
    
    dic = {}
    for i in range(len(friends)):
        name = friends[i]
        dic[name] = i
    
    # 주고받은 선물 arr & 선물지수 arr2를 초기화
    # a: 준 사람, b: 받은 사람
    for names in gifts:
        a,b = names.split()
        ai, bi = dic[a], dic[b]
        arr[ai][bi] += 1
        arr2[ai][0] += 1
        arr2[bi][1] += 1
    
    for i in range(N):
        arr2[i][2] = arr2[i][0] - arr2[i][1]

        
    result_arr = [0]*N

    for i in range(N-1):
        for j in range(i+1,N):
            # 주고받은 기록 있다면
            if arr[i][j]+arr[j][i]>0 and arr[i][j]!=arr[j][i]:
                # 많이 선물한 사람이 받기
                if arr[i][j] > arr[j][i]:
                    result_arr[i] += 1
                elif arr[j][i] > arr[i][j]:
                    result_arr[j] += 1
            # 주고받은 기록 x or 수가 같아    
            elif arr[i][j]+arr[j][i]==0 or arr[i][j]==arr[j][i]:
                # 선물 지수 큰 사람이 받기
                if arr2[i][2] > arr2[j][2]:
                    result_arr[i] += 1
                elif arr2[j][2] > arr2[i][2]:
                    result_arr[j] += 1
    print(result_arr)
    answer = max(result_arr)
    
    return answer