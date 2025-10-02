def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = [0] * bridge_length
    
    while truck_weights:
        on_bridge.pop(0)
        
        if sum(on_bridge) + truck_weights[0] <= weight:
            on_bridge.append(truck_weights[0])
            truck_weights.pop(0)
        else:
            on_bridge.append(0)
        
        # 시간 += 1
        answer += 1
        
    # 대기 중인 트럭 없으면 다리를 건너는 트럭에서 가장 뒤에 있는 트럭의 (인덱스+1)을 시간에 더하기
    for idx in range(bridge_length-1, -1, -1):
        if on_bridge[idx] != 0:
            answer += (idx+1)
            break
                
    return answer