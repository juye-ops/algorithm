from collections import Counter

dice = dict(Counter(list(map(int, input().split()))))
dice = list(dice.items())
if len(dice) == 1:
    print(dice[0][0] * 1000 + 10000)
elif len(dice) == 2:
    dice = sorted(dice, key=lambda x: x[1], reverse=True)
    print(dice[0][0] * 100 + 1000)
elif len(dice) == 3:
    dice = sorted(dice, key=lambda x: x[0], reverse=True)
    print(dice[0][0]*100)