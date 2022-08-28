def solution(new_id):
    regex = "-_."
    cnt = 0
    new_id = str(new_id)
    answer = new_id.lower()
    for i in answer:
        if (not i.isalpha()) and (not i.isdigit()) and (i not in regex):
            print(i)
            answer = answer.replace(i, "")


    while '..' in answer:
        answer = answer.replace('..', '.')


    answer = answer.strip(".")[:15].strip(".")

    if not answer: answer = "a"

    if len(answer) < 3:
        while(len(answer) < 3):
            answer+=answer[-1]

    return answer