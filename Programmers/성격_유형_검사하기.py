def solution(survey, choices):
    answer = ''
    mbti = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}
    choices = list(map(lambda x: x-4, choices))
    for i in range(len(survey)):
        if survey[i] not in mbti.keys():
            choices[i] *= -1
            survey[i] = survey[i][::-1]
    for s, score in zip(survey, choices):
        mbti[s] += score
    
    
    for i in mbti:
        answer+=i[0 if mbti[i]<=0 else 1]

    return answer