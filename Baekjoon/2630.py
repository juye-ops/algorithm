def check(board):
    val = board[0][0]
    for i in board:
        for j in i:
            if j != val:
                return False
    return True

def solution(N, board, answer=[0, 0]):
    if N == 1 or check(board):
        answer[board[0][0]] += 1
        return answer
    
    for i in range(4):
        if i == 0:
            next_board = [x[:(N//2)] for x in board[:(N//2)]]
        elif i == 1:
            next_board = [x[(N//2):] for x in board[:(N//2)]]
        elif i == 2:
            next_board = [x[:(N//2)] for x in board[(N//2):]]
        elif i == 3:
            next_board = [x[(N//2):] for x in board[(N//2):]]
        
        solution(N//2, next_board, answer)
    return answer

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(*solution(N, board), sep='\n')