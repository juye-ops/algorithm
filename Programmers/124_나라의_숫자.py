def solution(n):
    answer = ''
    lst = []
    dct = {0: "1", 1: "2", 2: "4"}
    while True:
        n-=1
        lst.append(n % 3)
        n = n//3
        if n <= 0:
            break
    lst.reverse()
    
    return "".join(list(map(lambda x: dct[x], lst)))