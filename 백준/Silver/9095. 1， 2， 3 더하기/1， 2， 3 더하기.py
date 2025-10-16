T = int(input())

for _ in range(T):
    N = int(input())
    dp1, dp2, dp3 = [0]*(N+1), [0]*(N+1), [0]*(N+1)
    
    # 초기화
    dp1[1] = 1
    if N>=2:
        dp1[2], dp2[2] = dp1[1], 1
    if N>=3:
        dp1[3] = dp1[2] + dp2[2]
        dp2[3] = dp2[2]
        dp3[3] = 1

    # 점화식
    if N>=3:
        for i in range(4,N+1):
            dp1[i] = dp1[i-1] + dp2[i-1] + dp3[i-1]
            dp2[i] = dp1[i-2] + dp2[i-2] + dp3[i-2]
            dp3[i] = dp1[i-3] + dp2[i-3] + dp3[i-3]

    answer = dp1[N] + dp2[N] + dp3[N]
    print(answer)