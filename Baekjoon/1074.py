def solution(N, r, c, answer = 0):  # r = y좌표, c = x좌표
    if r == c == 0:
        return answer
    
    length = 2**N
    
    new_r = r % (length//2)
    new_c = c % (length//2)
    
    quad_y = r // (length//2)
    quad_x = c // (length//2)
    
    # 2*quad_y + quad_x == 0~3 사이 범위로, 다음 사분면 중 시작점을 표시
    
    answer += ((length * length) // 4) * (2*quad_y + quad_x)
    
    return solution(N-1, new_r, new_c, answer)

N, r, c = map(int, input().split())

print(solution(N, r, c))

# 3 7 7
# 63

# 3 2 4
# 24