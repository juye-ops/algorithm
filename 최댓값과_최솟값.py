def solution(s):
    lst = sorted(list(map(int, s.split(" "))))
    answer = f"{lst[0]} {lst[-1]}"
    return answer