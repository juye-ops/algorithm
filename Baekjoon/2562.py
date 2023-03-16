def solution(lst):
    a, b = 0, 0
    for i, x in enumerate(lst):
        if x > a:
            a = x
            b = i+1
            
    return f"{a}\n{b}"

lst = [int(input()) for _ in range(9)]
print(solution(lst))