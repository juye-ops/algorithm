import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [tuple(map(int, input().split())) for _ in range(N)]

board = board + list(zip(*board))
answer = 0

for b in board:
    now = None
    length = 0
    for step in b:
        if now is None:
            now = step
            length = 1
            continue
        
        if step == now:
            length += 1
        
        elif step == now+1: # 오르막길
            if length < L:
                break
            length = 1
            now = step

        elif step == now-1: # 내리막길
            if length < 0:
                break
            length = -L+1
            now = step
        else: break
    else:
        if length < 0:
            continue
        answer += 1

print(answer)