from collections import deque

def solution(edges):
    # 생성한 정점의 번호,
    # 정점을 생성하기 전 도넛 수, 막대 수, 8자 수
    answer = [0]*4
    
    # 크기 n의 도넛 모양
    # n개의 정점, n개의 간선
    # 모든 정점은 1개의 간선만 가진다
    
    # 크기 n의 막대 모양
    # n개의 정점, n-1개의 간선
    # 모든 정점은 1개의 간선(마지막만 0개)만 가진다
    
    # 크기 n의 8자 모양
    # 2n+1개의 정점, 2n+2개의 간선
    # 크기 n+1의 도넛 모양을 결합한 모양
    # 한 정점만 2개의 간선, 나머지는 1개의 간선을 가진다
    
    N = max([x[0] for x in edges]+[x[1] for x in edges])
    send = [0]*(N+1)
    recv = [0]*(N+1)
    
    for v1, v2 in edges:
        # v1 -> v2
        send[v1] += 1
        recv[v2] += 1
    
    
    for i in range(1,N+1):
        # 생성한 노드: 어떤 정점 send 2 이상, recv 0
        if send[i]>=2 and recv[i]==0:
            answer[0] = i
        # 막대 모양: 마지막 정점은 send 0, recv 1 이상
        if send[i]==0 and recv[i]>0:
            answer[2] += 1
        # 8자 모양: 가운데 정점 send 2, recv 2 이상
        if send[i]==2 and recv[i]>=2:
            answer[3] += 1
    # 도넛 모양:
    answer[1] = send[answer[0]] - answer[2] - answer[3]
    
    return answer