def solution(x, y, w, h):
    return min([w-x, x, h-y, y])

print(solution(*map(int, input().split())))