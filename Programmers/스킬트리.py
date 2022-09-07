def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        ptr = 0
        for j in range(len(i)):
            if skill[ptr] == i[j]:
                ptr+=1
            elif i[j] in skill[ptr+1:]:
                break

            if ptr>=len(skill) or j == len(i)-1:
                answer+=1
                break

    return answer
