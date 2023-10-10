from heapq import *

n, m, k = map(int, input().split())
# g = gun
gboard = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(n):
        if gboard[i][j] == '0':
            gboard[i][j] = []
        else:
            gboard[i][j] = [-int(gboard[i][j])]

# a = player
pboard = [[0 for _ in range(n)] for _ in range(n)]
ppos = {}   # a: (x, y)
pdirection = {} # a: n
pstat = {}  # a: (초기 스탯, 무기 스탯)

answer = []

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for i in range(1, m+1):
    y, x, d, s = map(int, input().split())
    x, y = x-1, y-1

    pboard[y][x] = i
    ppos[i] = (x, y)
    pdirection[i] = d
    pstat[i] = (s, 0)
    answer.append(0)

def move_player(player, x, y, d):
    if not(0 <= x+dx[d] < n and 0 <= y+dy[d] < n):
        d = (d+2)%4
        pdirection[player] = d
    return x+dx[d], y+dy[d]

def get_weapon(player):
    basic, weapon = pstat[player]
    x, y = ppos[player]
    if gboard[y][x]:
        if weapon:
            heappush(gboard[y][x], -weapon)
        pstat[player] = (basic, -heappop(gboard[y][x]))

def loser_do(player):
    x, y = ppos[player]
    d = pdirection[loser]
    # 무기 해제
    basic, weapon = pstat[player]
    if weapon:
        heappush(gboard[y][x], -weapon)
    pstat[player] = (basic, 0)

    while not(0 <= x+dx[d] < n and 0 <= y+dy[d] < n) or pboard[y+dy[d]][x+dx[d]]:
        d = (d+1)%4
        pdirection[player] = d
        
    nx, ny = x+dx[d], y+dy[d]

    ppos[player] = (nx, ny)
    pboard[ny][nx] = loser
    # 패자 이동 후 무기 습득
    get_weapon(player)


def winner_do(player):
    get_weapon(player)

for round in range(k):
    for a in range(1, m+1):
        x, y = ppos[a]
        d = pdirection[a]
        # 1-1. 플레이어 이동
        nx, ny = move_player(a, x, y, d)
        pboard[y][x] = 0
        ppos[a] = (nx, ny)

        # 2-1. 무기 교체
        b = pboard[ny][nx] # 이동 후 바닥 or 상대편
        if not b: # 바닥
            pboard[ny][nx] = a
            get_weapon(a)
        
        # 2-2. 대결
        elif b:
            winner = loser = None
            reward = abs(sum(pstat[a]) - sum(pstat[b]))

            if sum(pstat[a]) == sum(pstat[b]): # 무승부 시 초기 스탯으로 승부
                if pstat[a][0] > pstat[b][0]:
                    winner = a
                    loser = b
                elif pstat[a][0] < pstat[b][0]:
                    winner = b
                    loser = a
            elif sum(pstat[a]) > sum(pstat[b]): # a 승리
                winner = a
                loser = b
            elif sum(pstat[a]) < sum(pstat[b]): # b 승리
                winner = b
                loser = a

            pboard[ny][nx] = winner
            
            # 패자 무기 버려
            loser_do(loser)
            winner_do(winner)
            answer[winner-1] += reward
        

print(*answer, sep=" ")