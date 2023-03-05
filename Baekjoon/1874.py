def solution(N, target):
    answer = ""
    stack = []
    ptr = 0
    for i in range(1, N+1):
        stack.append(i)
        answer+="+\n"
        while stack and target and stack[-1] == target[ptr]:
            stack.pop()
            ptr+=1
            answer+="-\n"

    return answer if ptr == N else "NO"

N = int(input())
target = [int(input()) for _ in range(N)]

print(solution(N, target))

# sys.stdin.readline()으로 풀면 매우 더 빨라짐