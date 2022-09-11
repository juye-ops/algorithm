def to_binary(a, b, width):
    return bin(a|b).replace("0b", "").zfill(width).replace("1", "#").replace("0", " ")

def solution(n, arr1, arr2):
    answer = []
    for pos in zip(arr1, arr2):
        answer.append(to_binary(*pos, n))

    return answer