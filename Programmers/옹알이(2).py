def solution(babbling):
    answer = []

    able = [("aya", "A"), ("ye", "B"), ("woo", "C"), ("ma", "D")]

    for i in babbling:
        for j in able:
            i = i.replace(*j)

        if not i.isupper():
            answer.append(False)
        else:
            trig = True
            for j in range(1, len(i)):
                if i[j] == i[j-1]:
                    trig = False
            answer.append(trig)

    return sum(answer)


print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))