from itertools import combinations

def solution(number):
    answer = len(list(filter(lambda x: sum(x) == 0, combinations(number, 3))))
    return answer