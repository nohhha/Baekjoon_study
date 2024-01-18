from collections import deque

def solution(n, edge):
    answer = 0
    graph=[[] for _ in range(n+1)]
    distance = [-1]*(n+1)
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    queue = deque([1])
    distance[1]=0
    
    while queue:
        now = queue.popleft() 
        for i in graph[now]:
            if distance[i]==-1: #아직 방문하지 않은 노드인 경우
                queue.append(i) #queue에 추가
                distance[i] = distance[now]+1 #거리 추가
    for d in distance:
        if d==max(distance):
            answer+=1
    return answer