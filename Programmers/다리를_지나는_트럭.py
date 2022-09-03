def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    time = 1
    sumval = 0
    while truck_weights:
        value = 0

        a = bridge.pop(0)
        sumval-=a
        if sumval + truck_weights[0] <= weight:
            value = truck_weights.pop(0)
        bridge.append(value)
        sumval+=value

        time+=1
    time+=bridge_length - 1
    return time

solution(2, 10, [7, 4, 5, 6])