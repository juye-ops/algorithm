a, b = 0, 1

for i in range(int(input())):
    c = (a+b)%15746
    a, b = b, c

print(c)