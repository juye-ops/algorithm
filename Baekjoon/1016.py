def solution(minimum, maximum):
    nosq = [True] * (maximum - minimum + 1)
    
    for i in range(2, int(maximum** 0.5) + 1):
        now = i**2
        for j in range(minimum//now*now - minimum, len(nosq), now):
            if 0<=j<=len(nosq):
                if nosq[j]:
                    nosq[j] = False

    return sum(nosq)
    

minimum, maximum = map(int, input().split())
print(solution(minimum, maximum))