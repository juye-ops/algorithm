import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

# u, d, l, r
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = 0

def move_up(board):
    global answer
    for i in range(N):
        j = 0
        while j < N:
            k = j+1

            if board[j][i] == 0: # most upper number attach to up side
                while k < N and board[k][i] == 0:
                    k+=1
                if k >= N:
                    break
                tmp = board[k][i]
                board[k][i] = board[j][i]
                board[j][i] = tmp

            answer = max(answer, board[j][i])

            while k < N and board[k][i] == 0:
                k+=1
            if k >= N:
                break

            if board[j][i] == board[k][i]:
                board[j][i] += board[k][i]
                board[k][i] = 0
                answer = max(answer, board[j][i])
            
            j += 1
    return board

def move_down(board):
    global answer
    for i in range(N):
        j = N-1
        while j > 0:
            k = j-1

            if board[j][i] == 0: # most upper number attach to up side
                while k >= 0 and board[k][i] == 0:
                    k-=1
                if k < 0:
                    break
                tmp = board[k][i]
                board[k][i] = board[j][i]
                board[j][i] = tmp

            answer = max(answer, board[j][i])

            while k >= 0 and board[k][i] == 0:
                k-=1
            if k < 0:
                break

            if board[j][i] == board[k][i]:
                board[j][i] += board[k][i]
                board[k][i] = 0
                answer = max(answer, board[j][i])
            
            j -= 1
    return board

def move_left(board):
    global answer
    for i in range(N):
        j = 0
        while j < N:
            k = j+1

            if board[i][j] == 0: # most left number attach to left side
                while k < N and board[i][k] == 0:
                    k+=1
                if k >= N:
                    break
                tmp = board[i][k]
                board[i][k] = board[i][j]
                board[i][j] = tmp

            answer = max(answer, board[j][i])

            while k < N and board[i][k] == 0:
                k+=1
            if k >= N:
                break

            if board[i][j] == board[i][k]:
                board[i][j] += board[i][k]
                board[i][k] = 0
                answer = max(answer, board[i][j])
            
            j += 1
    return board

def move_right(board):
    global answer
    for i in range(N):
        j = N-1
        while j > 0:
            k = j-1

            if board[i][j] == 0: # most right number attach to right side
                while k >= 0 and board[i][k] == 0:
                    k-=1
                if k < 0:
                    break
                tmp = board[i][k]
                board[i][k] = board[i][j]
                board[i][j] = tmp

            answer = max(answer, board[j][i])

            while k >= 0 and board[i][k] == 0:
                k-=1
            if k < 0:
                break

            if board[i][j] == board[i][k]:
                board[i][j] += board[i][k]
                board[i][k] = 0
                answer = max(answer, board[i][j])
            
            j -= 1
    return board

def dfs(board: list, cnt: int = 0):
    '''
    board: copied board
    cnt: count under 5 (default = 0)
    '''


    from copy import deepcopy
    if cnt == 5:
        return 
    dfs(move_up(deepcopy(board)), cnt+1)
    dfs(move_down(deepcopy(board)), cnt+1)
    dfs(move_left(deepcopy(board)), cnt+1)
    dfs(move_right(deepcopy(board)), cnt+1)

dfs(board)
print(answer)
