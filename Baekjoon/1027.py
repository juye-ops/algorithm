def is_possible(buildings, l, h):
    grad = (buildings[h] - buildings[l]) / (h - l)
    # y = slope * x + b
    # b = y - slope*x
    ## buildings[l] = slope * l + b
    ## buildings[h] = slope * h + b
    
    b = buildings[l] - (l*grad)
    
    for i in range(l+1, h):
        if grad * i + b <= buildings[i]:
            return False
    return True

def solution(N, buildings):
    answers = []
    for i in range(1, N+1):
        answer = 0
        for j in range(1, N+1):
            if j == i:
                continue
            # 두 건물 사이 건물이 방해하는가?
            l, h = min(i, j), max(i, j)
            
            answer += is_possible(buildings, l, h)
                
        answers.append(answer)
    return max(answers)

N = int(input())

buildings = [-1]+list(map(int, input().split()))

print(solution(N, buildings))

# print(is_possible(buildings, 1, 5))