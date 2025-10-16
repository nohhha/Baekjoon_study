def solution(begin, target, words):
    used = [0]*len(words)

    def dfs(cur, cnt):
        print('cur:',cur, 'cnt:',cnt, 'used:',used)
        if cur==target:
            print('target found')
            return cnt
        
        min_cnt = float('inf')
        for idx,word in enumerate(words):
            if used[idx]==1:
                continue
                
            diff_cnt = sum(c1!=c2 for c1,c2 in zip(cur,word))
            if diff_cnt == 1:
                used[idx]=1
                res = dfs(word, cnt+1)
                if res!=0:
                    min_cnt = min(min_cnt, res)
                used[idx]=0
        
        return 0 if min_cnt==float('inf') else min_cnt
    
    answer = dfs(begin, 0)
    return answer