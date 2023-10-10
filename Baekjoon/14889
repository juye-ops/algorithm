import sys
input = sys.stdin.readline

from itertools import combinations

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

teams = list(combinations(range(1, N+1), N//2))
team1 = teams[:len(teams)//2]
team2 = teams[:len(teams)//2-1:-1]

answer = int(1e9)

for t1, t2 in zip(team1, team2):
    t1_comb = list(combinations(t1, 2))
    t2_comb = list(combinations(t2, 2))
    a = 0
    b = 0
    for mem1, mem2 in t1_comb:
        a += board[mem1-1][mem2-1] + board[mem2-1][mem1-1]
    for mem1, mem2 in t2_comb:
        b += board[mem1-1][mem2-1] + board[mem2-1][mem1-1]

    answer = min(answer, abs(b-a))

print(answer)