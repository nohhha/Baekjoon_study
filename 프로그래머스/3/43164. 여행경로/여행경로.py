def solution(tickets):
    answer = []
        
    tickets.sort(key=lambda x: (x[0],x[1]))
    used = [0]*len(tickets)
    answer.append('ICN')
    
    def dfs(cur, used_cnt):
        if used_cnt==len(tickets):
            return answer

        for i, (dep, arv) in enumerate(tickets):
            if used[i]==0 and cur==dep:
                used[i]=1
                answer.append(arv)
                
                # 백트래킹
                res = dfs(arv, used_cnt + 1)
                if res is not None:
                    return res
                
                used[i]=0
                answer.pop()
        return None
    
    res = dfs('ICN', 0)
    return res    
