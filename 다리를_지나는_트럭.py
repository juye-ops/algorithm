def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    time = 1
    while truck_weights:
        value = 0

        bridge.pop(0)
        if sum(bridge) + truck_weights[0] <= weight:
            value = truck_weights.pop(0)
        bridge.append(value)

        time+=1
    time+=bridge_length - 1
    return time