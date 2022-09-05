def solution(a, b):
    answers = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    answer = 3
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(a-1):
        answer+=days[i]
    answer+=b
    
    return answers[answer%7]