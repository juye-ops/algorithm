x, y=input().split()
q, y=divmod(int(y)-45,60)
print((int(x)+q)%24, y)