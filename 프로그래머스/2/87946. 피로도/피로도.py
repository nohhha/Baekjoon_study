def dfs(k, cnt, dungeons):
    global answer, visited
    if cnt > answer:
        answer = cnt
    for i in range(len(dungeons)):
        if visited[i]==0 and k>=dungeons[i][0]:
            visited[i] = 1
            dfs(k-dungeons[i][1], cnt+1, dungeons)
            visited[i] = 0

            
def solution(k, dungeons):
    global answer, visited
    answer = 0
    visited = [0]*len(dungeons)     # 백트래킹
    dfs(k, 0, dungeons)
    
    return answer