import sys
input = sys.stdin.readline

tetromino = [
    ((0, 0), (0, 1), (0, 2), (0, 3)), # 일자
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    
    ((0, 0), (0, 1), (1, 0), (1, 1)), # 사각형
    
    ((1, 0), (1, 1), (0, 1), (0, 2)), # 역ㄹ 모양 
    ((0, 0), (1, 0), (1, 1), (2, 1)),
    
    ((0, 0), (0, 1), (1, 1), (1, 2)), # ㄹ 모양
    ((0, 1), (1, 1), (1, 0), (2, 0)),

    ((0, 0), (0, 1), (0, 2), (1, 1)), # T 모양
    ((0, 1), (1, 0), (1, 1), (1, 2)),
    ((1, 0), (0, 1), (1, 1), (2, 1)),
    ((0, 0), (1, 0), (2, 0), (1, 1)),

    ((0, 0), (0, 1), (0, 2), (1, 0)), # 역 ㄱ 모양
    ((0, 0), (0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 0), (1, 1), (1, 2)),
    ((0, 0), (1, 0), (2, 0), (2, 1)),

    ((0, 0), (0, 1), (0, 2), (1, 2)), # ㄱ 모양
    ((0, 1), (1, 1), (2, 1), (2, 0)),
    ((0, 0), (1, 0), (1, 1), (1, 2)),
    ((0, 0), (1, 0), (2, 0), (0, 1)),
]

def solution(N, M, board):
    answer = 0
    for i in range(N):
        for j in range(M):
            for t in tetromino:
                tmp = 0
                for ty, tx in t:
                    if 0 <= i+ty < N and 0 <= j+tx < M:
                        tmp += board[i+ty][j+tx]
                    else:
                        break
                else:
                    answer = max(answer, tmp)


    return answer


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))