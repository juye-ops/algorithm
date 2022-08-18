def solution(n):
    answer = 0
    for i in range(n):
        word = input()
        for j in range(len(word)-1):
            if word[j] != word[j+1] and word[j] in word[j+2:]:
                break
        else:
            answer+=1
            continue

    return answer
print(solution(int(input())))