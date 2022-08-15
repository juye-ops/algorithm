def solution(absolutes, signs):
    answer = sum([x * 2*(int(y)-0.5) for x,y in zip(absolutes, signs)])
    return answer