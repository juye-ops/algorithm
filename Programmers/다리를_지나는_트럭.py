def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    
    now = 0
    while True:
        val = bridge.pop(0)
        now -= val
        bridge.append(0)
        answer += 1
        
        if truck_weights and (now + truck_weights[0] <= weight):
            truck = truck_weights.pop(0)
            now += truck
            bridge[-1] = truck

        if now == 0:
            break
            
    return answer