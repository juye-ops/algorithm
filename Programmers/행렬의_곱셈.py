import numpy as np

def solution(arr1, arr2):
    answer = np.matmul(arr1, arr2)
    return answer.tolist()