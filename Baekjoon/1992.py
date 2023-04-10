def check(image):
    now = image[0][0]
    for i in image:
        for j in i:
            if j != now:
                return False
    return True

def solution(N, image, answer=[]):
    if check(image) or N == 1:
        answer.append(image[0][0])
        return "".join(answer)
    
    answer.append('(')
    for i in range(2):
        for j in range(2):
            next_N = N//2
            next_image = [x[j*next_N:(j+1)*next_N] for x in image[i*next_N:(i+1)*next_N]]
            solution(next_N, next_image, answer)
    answer.append(')')
    
    return "".join(answer)

N = int(input())
image = [input() for _ in range(N)]

print(solution(N, image))