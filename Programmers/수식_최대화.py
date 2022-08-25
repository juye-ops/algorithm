from itertools import permutations


def solution(expression):
    lst = []
    answers = []
    a = 0
    for i in range(len(expression)):
        if not expression[i].isdigit():
            lst.append(expression[a:i])
            lst.append(expression[i])
            a = i + 1
    lst.append(expression[a:i + 1])

    for i in list(permutations("*+-", 3)):
        n_lst = lst.copy()
        for j in i:
            k = 1
            while len(n_lst) > 1 and k < len(n_lst):
                if n_lst[k] == j:
                    n_lst.insert(k - 1, str(eval(n_lst.pop(k - 1) + n_lst.pop(k - 1) + n_lst.pop(k - 1))))
                    k = -1
                k += 2

        answers.append(abs(int(n_lst[0])))

    return max(answers)