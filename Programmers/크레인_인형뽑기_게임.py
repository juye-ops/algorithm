def solution(board, moves):
    new_board = {x+1: [] for x in range(len(board[0]))}
    stack = []
    for i in board:
        for j in range(len(i)):
            if i[j]: new_board[j+1].append(i[j])
    cnt = 0
    for i in moves:
        if new_board[i]:
            a = new_board[i].pop(0)
            if stack and a == stack[-1]:
                stack.pop()
                cnt+=1
            else:stack.append(a)
    return cnt*2