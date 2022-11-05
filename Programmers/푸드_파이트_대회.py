def solution(food):
    answer = "0"
    food = list(map(lambda x: x//2, food))


    for i, x in enumerate(food[:0:-1]):
        for j in range(x):
            answer = answer + str(len(food) - i - 1)
            answer = str(len(food) - i - 1) + answer
    return answer