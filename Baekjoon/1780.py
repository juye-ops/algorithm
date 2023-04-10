import sys
input = sys.stdin.readline

import numpy as np

# Python list
def check(paper):
    now = paper[0][0]
    for i in paper:
        for j in i:
            if j != now:
                return False
    return True

def dfs(N, paper, answer = {-1: 0, 0: 0, 1: 0}):
    if N == 1 or check(paper):
        answer[paper[0][0]]+=1
        return answer.values()
    
    for i in range(3):
        for j in range(3):
            next_N = N//3
            next_paper = [x[j*(N//3):(j+1)*(N//3)] for x in paper[i*(N//3):(i+1)*(N//3)]]
            dfs(next_N, next_paper, answer)

    return answer.values()
    
def solution(N, paper):
    answer = dfs(N, paper)
    for i in answer:
        print(i)



# Py List solution
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
solution(N, paper)


# Numpy
def np_check(paper):
    now = paper[0][0]
    return np.all(paper == now)

def np_dfs(N, paper, answer = {-1: 0, 0: 0, 1: 0}):
    if N == 1 or check(paper):
        answer[paper[0][0]]+=1
        return answer.values()
    
    for i in range(3):
        for j in range(3):
            next_N = N//3
            next_paper = paper[i*(N//3):(i+1)*(N//3), j*(N//3):(j+1)*(N//3)]
            dfs(next_N, next_paper, answer)

    return answer.values()
    
def np_solution(N, paper):
    answer = np_dfs(N, paper)
    for i in answer:
        print(i)

np_paper = np.array(paper)

# Numpy solution
np_solution(N, np_paper)