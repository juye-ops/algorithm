from itertools import permutations


def solution(numbers):
    answer = list(map(sum, list(permutations(numbers, 2))))
    answer = sorted(list(set(answer)))
    return answer