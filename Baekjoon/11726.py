answers = [1, 2]

a = int(input())
for i in range(1, a):
    answers.append(sum(answers[-2:]))
print(answers[a-1]%10007)