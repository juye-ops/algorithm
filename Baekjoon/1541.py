def solution(maths):
    i=1
    while i < len(maths):
        if maths[i] == "+":
            maths = maths[:i-1] + [maths[i-1]+maths[i+1]] + maths[i+2:]
        else:
            i+=2
    

    i=1
    while i < len(maths):
        if maths[i] == "-":
            maths = maths[:i-1] + [maths[i-1]-maths[i+1]] + maths[i+2:]
        else:
            i+=2

    return maths[0]

math = input()
maths = []
start = 0
for i in range(len(math)):
    if not math[i].isdigit():
        maths.append(int(math[start:i]))
        maths.append(math[i])
        start = i+1
else:
    maths.append(int(math[start:]))

print(solution(maths))