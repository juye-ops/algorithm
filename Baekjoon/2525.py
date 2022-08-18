x, y=input().split()
dur = int(input())
q, y=divmod(int(y)+dur, 60)
print((int(x)+q)%24, y)