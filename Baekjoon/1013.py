import re

frequency = [input() for _ in range(int(input()))]

regex = re.compile("(100+1+|01)+")

for i in frequency:
    if regex.fullmatch(i):
        print("YES")

    else:
        print("NO")
