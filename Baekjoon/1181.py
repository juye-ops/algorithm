def solution(N, words):
    return "\n".join(sorted(sorted(words), key=len))

N = int(input())
words = {input() for _ in range(N)}

print(solution(N, words))