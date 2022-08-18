answers = [1, 2, 4]

for i in range(int(input())):
    find = int(input())
    while len(answers) <= find:
        answers.append(sum(answers[-3:]))
    print(answers[find-1])