input()
acid = sorted(list(map(int, input().split())))

left = 0
right = len(acid) - 1

minimum = None
while left < right:
    val = acid[left] + acid[right]
    if minimum==None or abs(val) < minimum:
        minimum = abs(val)
        min_ab = [acid[left], acid[right]]

    if val < 0:
        left+=1
    elif val > 0:
        right-=1
    else:
        break

print(str(min_ab).strip("[]").replace(",", ""))