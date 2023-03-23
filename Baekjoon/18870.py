def solution(N, pos):
    s_pos = sorted(pos)
    zipmap = {}
    for i in s_pos:
        if zipmap.get(i) is None:
            zipmap[i] = len(zipmap)
    
    return " ".join(map(lambda x: str(zipmap[x]), pos))

N = int(input())
pos = list(map(int, input().split()))

print(solution(N, pos))