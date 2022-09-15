def solution(inputs):
    targets = [1, 1, 2, 2, 2, 8]
    answer=""
    for i in range(6):
        answer+=f"{targets[i]-inputs[i]} "
    return answer

print(solution(list(map(int, input().split()))))