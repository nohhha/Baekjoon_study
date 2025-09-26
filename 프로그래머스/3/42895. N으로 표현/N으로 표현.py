def solution(N, number):
    answer = -1
    
    
    # dp[i] 는 N을 i번 사용해서 만들 수 있는 수의 set
    dp = [set() for _ in range(9)]
    dp[0].add(0)
    dp[1].add(N)
    
    if N==number:
        return 1
    
    for i in range(2,9):
        dp[i].add(N*(10**i-1)//9)
        for k in range(1,i):
            for n1 in dp[k]:
                for n2 in dp[i-k]:
                    dp[i].add(n1 + n2)
                    dp[i].add(n1 - n2)
                    dp[i].add(n1 * n2)
                    if n2!=0:
                        dp[i].add(n1 // n2)
        
        if number in dp[i]:
            return i
    
    return answer