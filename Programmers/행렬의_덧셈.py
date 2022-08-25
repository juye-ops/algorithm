def solution(arr1, arr2):
    return [[x+y for x, y in zip(i, j)] for i, j in zip(arr1, arr2) ]