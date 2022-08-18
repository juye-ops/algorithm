a = [0, 1]
for i in range(int(input())-1):
    a.append(sum(a[-2:]))
print(a[-1])